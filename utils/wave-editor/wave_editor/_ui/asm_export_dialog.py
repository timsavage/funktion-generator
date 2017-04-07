# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/asm_export_dialog.ui'
#
# Created: Sat Apr  8 00:53:01 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ASMExportDialog(object):
    def setupUi(self, ASMExportDialog):
        ASMExportDialog.setObjectName("ASMExportDialog")
        ASMExportDialog.setWindowModality(QtCore.Qt.WindowModal)
        ASMExportDialog.resize(330, 147)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ASMExportDialog.sizePolicy().hasHeightForWidth())
        ASMExportDialog.setSizePolicy(sizePolicy)
        ASMExportDialog.setMinimumSize(QtCore.QSize(330, 147))
        ASMExportDialog.setMaximumSize(QtCore.QSize(16777215, 147))
        self.gridLayout_2 = QtGui.QGridLayout(ASMExportDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(ASMExportDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.asmStyleCombo = QtGui.QComboBox(self.groupBox)
        self.asmStyleCombo.setObjectName("asmStyleCombo")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.asmStyleCombo)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.asmlabelEdit = QtGui.QLineEdit(self.groupBox)
        self.asmlabelEdit.setObjectName("asmlabelEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.asmlabelEdit)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ASMExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.label_2.setBuddy(self.asmStyleCombo)
        self.label.setBuddy(self.asmlabelEdit)

        self.retranslateUi(ASMExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ASMExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ASMExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ASMExportDialog)

    def retranslateUi(self, ASMExportDialog):
        ASMExportDialog.setWindowTitle(QtGui.QApplication.translate("ASMExportDialog", "ASM Export...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ASMExportDialog", "Output Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ASMExportDialog", "ASM Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("ASMExportDialog", "ASM Label used to reference the data table.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ASMExportDialog", "Label", None, QtGui.QApplication.UnicodeUTF8))

