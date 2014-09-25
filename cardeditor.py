import sys
import signal
from PyQt4 import QtGui, QtCore

from ui import Ui_Dialog

from msr import msr

class CardEditor(QtGui.QWidget):
    def __init__(self, device):
        QtGui.QWidget.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.dev = msr(device)

        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.eraseButton.clicked.connect(self.erase)
        self.ui.readButton.clicked.connect(self.read)
        self.ui.writeButton.clicked.connect(self.write)

        self.ui.track1Edit.returnPressed.connect(self.write)
        self.ui.track2Edit.returnPressed.connect(self.write)
        self.ui.track3Edit.returnPressed.connect(self.write)

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
        try:
            t1, t2, t3 = self.dev.read_tracks()
        except Exception as e:
            self.write_status(str(e))
        else:
            status = []   

            if t1:
                status.append("Track 1: {}".format(t1))

            if t2:
                status.append("Track 2: {}".format(t2))

            if t3:
                status.append("Track 3: {}".format(t3))

            self.write_status("\n".join(status))

    def write(self):
        t1 = self.ui.track1Edit.text().toAscii()
        t2 = self.ui.track2Edit.text().toAscii()
        t3 = self.ui.track3Edit.text().toAscii()

        self.ui.track1Edit.clear()
        self.ui.track2Edit.clear()
        self.ui.track3Edit.clear()

        self.dev.write_tracks(t1, t2, t3)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = CardEditor('/dev/ttyUSB0')

    window.show()

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
