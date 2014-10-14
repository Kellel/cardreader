# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardeditor.ui'
#
# Created: Tue Oct 14 14:40:25 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 359)
        self.deviceEdit = QtGui.QLineEdit(Dialog)
        self.deviceEdit.setGeometry(QtCore.QRect(20, 310, 271, 30))
        self.deviceEdit.setObjectName(_fromUtf8("deviceEdit"))
        self.deviceButton = QtGui.QPushButton(Dialog)
        self.deviceButton.setGeometry(QtCore.QRect(310, 310, 121, 28))
        self.deviceButton.setObjectName(_fromUtf8("deviceButton"))
        self.statusEdit = QtGui.QPlainTextEdit(Dialog)
        self.statusEdit.setGeometry(QtCore.QRect(20, 20, 411, 201))
        self.statusEdit.setReadOnly(True)
        self.statusEdit.setObjectName(_fromUtf8("statusEdit"))
        self.resetButton = QtGui.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(460, 20, 151, 41))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.eraseButton = QtGui.QPushButton(Dialog)
        self.eraseButton.setGeometry(QtCore.QRect(460, 80, 151, 41))
        self.eraseButton.setObjectName(_fromUtf8("eraseButton"))
        self.readtracksButton = QtGui.QPushButton(Dialog)
        self.readtracksButton.setGeometry(QtCore.QRect(460, 140, 151, 81))
        self.readtracksButton.setObjectName(_fromUtf8("readtracksButton"))
        self.writetracksButton = QtGui.QPushButton(Dialog)
        self.writetracksButton.setGeometry(QtCore.QRect(460, 240, 151, 101))
        self.writetracksButton.setObjectName(_fromUtf8("writetracksButton"))
        self.track3Edit = QtGui.QLineEdit(Dialog)
        self.track3Edit.setGeometry(QtCore.QRect(300, 260, 131, 30))
        self.track3Edit.setObjectName(_fromUtf8("track3Edit"))
        self.track2Edit = QtGui.QLineEdit(Dialog)
        self.track2Edit.setGeometry(QtCore.QRect(160, 260, 131, 30))
        self.track2Edit.setObjectName(_fromUtf8("track2Edit"))
        self.track1Edit = QtGui.QLineEdit(Dialog)
        self.track1Edit.setGeometry(QtCore.QRect(20, 260, 131, 30))
        self.track1Edit.setObjectName(_fromUtf8("track1Edit"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 77, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 240, 77, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(340, 240, 77, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.deviceButton.setText(_translate("Dialog", "Set Device", None))
        self.resetButton.setText(_translate("Dialog", "Reset", None))
        self.eraseButton.setText(_translate("Dialog", "Erase", None))
        self.readtracksButton.setText(_translate("Dialog", "Read Tracks", None))
        self.writetracksButton.setText(_translate("Dialog", "Write Tracks", None))
        self.label_4.setText(_translate("Dialog", "Track 1", None))
        self.label_5.setText(_translate("Dialog", "Track 2", None))
        self.label_6.setText(_translate("Dialog", "Track 3", None))

