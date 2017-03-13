# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/main_window.ui'
#
# Created: Tue Mar 14 09:16:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 644)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(65, 123, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtGui.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuWaveForm = QtGui.QMenu(self.menubar)
        self.menuWaveForm.setObjectName("menuWaveForm")
        self.menuGenerate = QtGui.QMenu(self.menuWaveForm)
        self.menuGenerate.setObjectName("menuGenerate")
        self.menuMergeWith = QtGui.QMenu(self.menuWaveForm)
        self.menuMergeWith.setObjectName("menuMergeWith")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSine = QtGui.QAction(MainWindow)
        self.actionSine.setObjectName("actionSine")
        self.actionSquare = QtGui.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionTriangle = QtGui.QAction(MainWindow)
        self.actionTriangle.setObjectName("actionTriangle")
        self.actionSawtooth = QtGui.QAction(MainWindow)
        self.actionSawtooth.setObjectName("actionSawtooth")
        self.actionReverseSawtooth = QtGui.QAction(MainWindow)
        self.actionReverseSawtooth.setObjectName("actionReverseSawtooth")
        self.actionZero = QtGui.QAction(MainWindow)
        self.actionZero.setObjectName("actionZero")
        self.actionInvert = QtGui.QAction(MainWindow)
        self.actionInvert.setObjectName("actionInvert")
        self.actionMirror = QtGui.QAction(MainWindow)
        self.actionMirror.setObjectName("actionMirror")
        self.actionASMDataTable = QtGui.QAction(MainWindow)
        self.actionASMDataTable.setObjectName("actionASMDataTable")
        self.actionCDatatable = QtGui.QAction(MainWindow)
        self.actionCDatatable.setObjectName("actionCDatatable")
        self.actionMergeSine = QtGui.QAction(MainWindow)
        self.actionMergeSine.setObjectName("actionMergeSine")
        self.actionMergeSquare = QtGui.QAction(MainWindow)
        self.actionMergeSquare.setObjectName("actionMergeSquare")
        self.actionMergeTriangle = QtGui.QAction(MainWindow)
        self.actionMergeTriangle.setObjectName("actionMergeTriangle")
        self.actionMergeSawtooth = QtGui.QAction(MainWindow)
        self.actionMergeSawtooth.setObjectName("actionMergeSawtooth")
        self.actionMergeReverseSawtooth = QtGui.QAction(MainWindow)
        self.actionMergeReverseSawtooth.setObjectName("actionMergeReverseSawtooth")
        self.menuExport.addAction(self.actionASMDataTable)
        self.menuExport.addAction(self.actionCDatatable)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuGenerate.addAction(self.actionSine)
        self.menuGenerate.addAction(self.actionSquare)
        self.menuGenerate.addAction(self.actionTriangle)
        self.menuGenerate.addAction(self.actionSawtooth)
        self.menuGenerate.addAction(self.actionReverseSawtooth)
        self.menuMergeWith.addAction(self.actionMergeSine)
        self.menuMergeWith.addAction(self.actionMergeSquare)
        self.menuMergeWith.addAction(self.actionMergeTriangle)
        self.menuMergeWith.addAction(self.actionMergeSawtooth)
        self.menuMergeWith.addAction(self.actionMergeReverseSawtooth)
        self.menuWaveForm.addAction(self.actionZero)
        self.menuWaveForm.addAction(self.menuGenerate.menuAction())
        self.menuWaveForm.addAction(self.menuMergeWith.menuAction())
        self.menuTools.addAction(self.actionInvert)
        self.menuTools.addAction(self.actionMirror)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWaveForm.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Wave Table Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWaveForm.setTitle(QtGui.QApplication.translate("MainWindow", "&Wave Form", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGenerate.setTitle(QtGui.QApplication.translate("MainWindow", "&Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMergeWith.setTitle(QtGui.QApplication.translate("MainWindow", "&Merge with", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSine.setText(QtGui.QApplication.translate("MainWindow", "Sine", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSine.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSquare.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSquare.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTriangle.setText(QtGui.QApplication.translate("MainWindow", "Triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTriangle.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSawtooth.setText(QtGui.QApplication.translate("MainWindow", "Sawtooth", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSawtooth.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReverseSawtooth.setText(QtGui.QApplication.translate("MainWindow", "Reverse Sawtooth", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReverseSawtooth.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZero.setText(QtGui.QApplication.translate("MainWindow", "&Zero", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZero.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+0", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvert.setText(QtGui.QApplication.translate("MainWindow", "&Invert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInvert.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirror.setText(QtGui.QApplication.translate("MainWindow", "&Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirror.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionASMDataTable.setText(QtGui.QApplication.translate("MainWindow", "ASM Data table...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionASMDataTable.setToolTip(QtGui.QApplication.translate("MainWindow", "Export to ASM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionASMDataTable.setStatusTip(QtGui.QApplication.translate("MainWindow", "Export the wave as a data table for GCC Assember.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCDatatable.setText(QtGui.QApplication.translate("MainWindow", "C Data table...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeSine.setText(QtGui.QApplication.translate("MainWindow", "Sine", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeSine.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeSquare.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeSquare.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+@", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeTriangle.setText(QtGui.QApplication.translate("MainWindow", "Triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeTriangle.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+#", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeSawtooth.setText(QtGui.QApplication.translate("MainWindow", "Sawtooth", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeSawtooth.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+$", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeReverseSawtooth.setText(QtGui.QApplication.translate("MainWindow", "Reverse Sawtooth", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMergeReverseSawtooth.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+%", None, QtGui.QApplication.UnicodeUTF8))

