import sys
import signal
from PyQt4 import QtGui, QtCore

from ui import Ui_Dialog
from worker import Worker

class CardEditor(QtGui.QWidget):
    def __init__(self, device):
        QtGui.QWidget.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.device = "/dev/ttyUSB0"
        self.worker = Worker(self.device)
        self.current = None

        # Advanced View
        self.ui.readtracksButton.clicked.connect(self.read_tracks)
        self.ui.writetracksButton.clicked.connect(self.write_tracks)

        self.ui.deviceEdit.setText(self.device)
        self.ui.deviceButton.clicked.connect(self.set_device)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.read_device)
        self.timer.start()

    def closeEvent(self, event):
        self.timer.stop()
        self.worker.terminate()
        event.accept()

    def write_status(self, msg, msg2 = None, msg3 = None):
        self.ui.statusEdit.moveCursor(QtGui.QTextCursor.End)


        if msg2 and msg3:
            self.ui.statusEdit.insertPlainText("{}  {}  {}\n".format(msg, msg2, msg3))
        else:
            self.ui.statusEdit.insertPlainText(msg + '\n')

        self.ui.statusEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.statusEdit.ensureCursorVisible()

    def reset(self):
        self.worker.reset()
        self.write_status("[Sent RESET]")

    def erase(self):
        self.worker.erase()
        self.write_status("[Sent ERASE]")

    def read_tracks(self):
        self.worker.read_tracks()
        self.write_status("[Sent READTRACKS]")

    def write_tracks(self):
        t1 = self.ui.track1Edit.text().toAscii() or None
        t2 = self.ui.track2Edit.text().toAscii() or None
        t3 = self.ui.track3Edit.text().toAscii() or None

        if t1 or t2 or t3:

            self.worker.writetracks(str(t1), str(t2), str(t3))
            self.write_status("[Sent WRITETRACKS]")

            self.ui.track1Edit.clear()
            self.ui.track2Edit.clear()
            self.ui.track3Edit.clear()

    def read_device(self):
        status, result = self.worker.get_status()
        
        while status:
            if result:
                self.write_status("{}: {}".format(status, result))
            else:
                self.write_status(status)
            status, result = self.worker.get_status()

    def set_device(self):
        self.device = str(self.ui.deviceEdit.text().toAscii())
        self.timer.stop()
        self.worker.terminate()
        del self.worker
        self.worker = Worker(self.device)
        self.timer.start()

        self.write_status("[Device {}]".format(self.device))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = CardEditor('/dev/ttyUSB0')

    window.show()

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
