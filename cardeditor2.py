import sys
import signal
from PyQt4 import QtGui, QtCore

from ui import Ui_Dialog
from parse_api import Parse

from worker import Worker

class CardEditor(QtGui.QWidget):
    def __init__(self, device):
        QtGui.QWidget.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.worker = Worker("/dev/ttyUSB0")
        self.parse = Parse()

        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.eraseButton.clicked.connect(self.erase)
        self.ui.readButton.clicked.connect(self.read)
        self.ui.writeButton.clicked.connect(self.write)

        self.ui.track1Edit.returnPressed.connect(self.write)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.read_device)
        self.timer.start()

    def closeEvent(self, event):
        self.timer.stop()
        self.worker.terminate()
        event.accept()

    def write_status(self, msg):
        self.ui.statusEdit.insertPlainText(msg + '\n')
        self.ui.statusEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.statusEdit.ensureCursorVisible()

    def reset(self):
        self.worker.reset()
        self.write_status("[Sent RESET]")

    def erase(self):
        self.worker.erase()
        self.write_status("[Sent ERASE]")

    def read(self):
        self.worker.read()
        self.write_status("[Sent READ]")

    def write(self):
        username = self.ui.track1Edit.text().toAscii()

        user = self.parse.getUserByUsername(str(username))

        if user:
            print(user)
            phone = user['phone'] if 'phone' in user else user['phone1'] if 'phone1' in user else ""
            status = "User {} found. Phone: {}".format(user['usernameDisplay'], phone)
            self.write_status(status)
            self.worker.write(str(user['userId']))
        else:
            self.write_status("User lookup failed!")

        self.ui.track1Edit.clear()

    def read_device(self):
        status, result = self.worker.get_status()
        
        while status:
            if result:
                self.write_status("{}: {}".format(status, result))
            else:
                self.write_status(status)
            status, result = self.worker.get_status()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = CardEditor('/dev/ttyUSB0')

    window.show()

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
