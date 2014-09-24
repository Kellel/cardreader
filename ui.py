# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardeditor.ui'
#
# Created: Wed Sep 10 17:17:21 2014
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
        Dialog.resize(640, 343)
        self.statusEdit = QtGui.QPlainTextEdit(Dialog)
        self.statusEdit.setGeometry(QtCore.QRect(10, 10, 471, 261))
        self.statusEdit.setReadOnly(True)
        self.statusEdit.setObjectName(_fromUtf8("statusEdit"))
        self.resetButton = QtGui.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(500, 10, 131, 61))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.eraseButton = QtGui.QPushButton(Dialog)
        self.eraseButton.setGeometry(QtCore.QRect(500, 80, 131, 61))
        self.eraseButton.setObjectName(_fromUtf8("eraseButton"))
        self.readButton = QtGui.QPushButton(Dialog)
        self.readButton.setGeometry(QtCore.QRect(500, 150, 131, 121))
        self.readButton.setObjectName(_fromUtf8("readButton"))
        self.track1Edit = QtGui.QLineEdit(Dialog)
        self.track1Edit.setGeometry(QtCore.QRect(10, 290, 341, 41))
        self.track1Edit.setObjectName(_fromUtf8("track1Edit"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 270, 621, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.writeButton = QtGui.QPushButton(Dialog)
        self.writeButton.setGeometry(QtCore.QRect(360, 290, 271, 41))
        self.writeButton.setObjectName(_fromUtf8("writeButton"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(480, 10, 20, 271))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Card Editor", None))
        self.resetButton.setText(_translate("Dialog", "Reset", None))
        self.eraseButton.setText(_translate("Dialog", "Erase", None))
        self.readButton.setText(_translate("Dialog", "Read", None))
        self.writeButton.setText(_translate("Dialog", "Write", None))

