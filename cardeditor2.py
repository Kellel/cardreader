import sys
import signal
from PyQt4 import QtGui, QtCore

from ui import Ui_Dialog
from parse_api import Parse

from msr import msr

class CardEditor(QtGui.QWidget):
    def __init__(self, device):
        QtGui.QWidget.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.dev = msr(device)
        self.parse = Parse()

        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.eraseButton.clicked.connect(self.erase)
        self.ui.readButton.clicked.connect(self.read)
        self.ui.writeButton.clicked.connect(self.write)

        self.ui.track1Edit.returnPressed.connect(self.write)

    def write_status(self, msg):
        self.ui.statusEdit.insertPlainText(msg + '\n')
        self.ui.statusEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.statusEdit.ensureCursorVisible()

    def reset(self):
        self.dev.reset()
        self.write_status("Device Reset!")

    def erase(self):
        self.dev.erase_tracks(True, True, True)
        self.write_status("Card Erased!")

    def read(self):
        status = ""
        try:
            _, t2,_  = self.dev.read_tracks()
        except Exception as e:
            self.write_status(str(e))
        else:
            if t2:
                t2 = t2[1:len(t2)-1]
                print (t2)
                user = self.parse.getUserById(str(t2))
                if user:
                    status = "User {} Found".format(user['usernameDisplay'])
                else:
                    status = "User not Found"
            else:
                status = "No Card Data"

            self.write_status(status + '\n')

    def write(self):
        username = self.ui.track1Edit.text().toAscii()

        user = self.parse.getUserByUsername(str(username))

        if user:
            print(user)
            phone = user['phone'] if 'phone' in user else user['phone1'] if 'phone1' in user else ""
            status = "User {} found. Phone: {}".format(user['usernameDisplay'], phone)
            self.write_status(status)
            self.dev.write_tracks(t2 = str(user['userId']))
        else:
            self.write_status("User lookup failed!")

        self.ui.track1Edit.clear()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = CardEditor('/dev/ttyUSB0')

    window.show()

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
