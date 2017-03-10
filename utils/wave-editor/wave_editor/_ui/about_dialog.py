# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/about_dialog.ui'
#
# Created: Fri Mar 10 15:23:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(400, 150)
        AboutDialog.setMinimumSize(QtCore.QSize(360, 110))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 150))
        AboutDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        AboutDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        AboutDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(AboutDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutDialog", "Open Funktion Gen\n"
"Wavetable Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AboutDialog", "Copyright 2017 Tim Savage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AboutDialog", "https://github.com/timsavage/funktion-generator", None, QtGui.QApplication.UnicodeUTF8))

