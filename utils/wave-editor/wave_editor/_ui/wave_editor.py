# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/wave_editor.ui'
#
# Created: Tue Mar  7 22:14:09 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditorWindow(object):
    def setupUi(self, EditorWindow):
        EditorWindow.setObjectName("EditorWindow")
        EditorWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(EditorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        EditorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditorWindow)
        QtCore.QMetaObject.connectSlotsByName(EditorWindow)

    def retranslateUi(self, EditorWindow):
        EditorWindow.setWindowTitle(QtGui.QApplication.translate("EditorWindow", "Wave Editor", None, QtGui.QApplication.UnicodeUTF8))

