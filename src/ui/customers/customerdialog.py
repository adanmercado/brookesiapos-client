from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import Qt, QTimer

from .customerdialog_ui import CustomerDialog_UI

class CustomerDialog(CustomerDialog_UI, QDialog):
    def __init__(self, parent: QWidget = None) -> None:
        super(CustomerDialog, self).__init__(parent)
        self.setup()

    def setup(self) -> None:
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.tr('Customer'))
        self.setModal(True)

        self.error_label.hide()

        self.accept_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def accept(self) -> None:
        if not self.keeppen_checkbox.isChecked():
            return super().accept()

    def show_error(self, message: str) -> None:
        self.error_label.setText(message)
        self.setFixedHeight(397)
        self.error_label.setVisible(True)

        QTimer.singleShot(3000, self.hide_error)

    def hide_error(self) -> None:
        self.error_label.setVisible(False)
        self.setFixedHeight(357)