from PySide import QtGui

from .._ui.about_dialog import Ui_AboutDialog
from .._ui.asm_export_dialog import Ui_ASMExportDialog
from ..wave_file import ExportAsmFormatter


class AboutDialog(QtGui.QDialog):
    """
    About dialog
    """
    @classmethod
    def display(cls):
        cls().exec_()

    def __init__(self):
        super(AboutDialog, self).__init__()

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)


class AsmExportDialog(QtGui.QDialog):
    """
    ASM export configuration dialog
    """
    @classmethod
    def getExportOptions(cls, asmStyle=None, asmLabel=None):
        dialog = cls()
        dialog.setAsmStyle(asmStyle or '')
        dialog.setAsmLabel(asmLabel or '')
        dialog.show()

        res = dialog.exec_()
        if res == 0:
            return None, None

        return dialog.getAsmStyle(), dialog.getAsmLabel()

    def __init__(self):
        super(AsmExportDialog, self).__init__()

        self.ui = Ui_ASMExportDialog()
        self.ui.setupUi(self)

        self.ui.asmStyleCombo.addItem("GCC ASM", ExportAsmFormatter.ASM_STYLE_GCC)
        self.ui.asmStyleCombo.addItem("AVR Assembler", ExportAsmFormatter.ASM_STYLE_AVRASM2)

    def setAsmStyle(self, asmStyle):
        pass

    def setAsmLabel(self, asmLabel):
        self.ui.asmlabelEdit.setText(asmLabel)

    def getAsmStyle(self):
        return self.ui.asmStyleCombo.currentIndex()

    def getAsmLabel(self):
        return self.ui.asmlabelEdit.text()
