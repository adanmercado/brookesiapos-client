from PySide6.QtWidgets import QWidget, QMessageBox, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

class MessageBox(QMessageBox):
    def __init__(self, type: QMessageBox.Icon = QMessageBox.Information, text: str = None, parent: QWidget = None) -> None:
        super(MessageBox, self).__init__(parent)
        self.setup(type, text)

    def setup(self, type: QMessageBox.Icon, text: str) -> None:
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setIcon(type)
        self.setText(text)
        self.setModal(True)

        accept_button = QPushButton(QIcon('qrc/icons/ok.png'), self.tr('Accept'), self)
        accept_button.setIconSize(QSize(32, 32))
        self.addButton(accept_button, QMessageBox.AcceptRole)

        if type == QMessageBox.Question:
            cancel_button = QPushButton(QIcon('qrc/icons/cancel.png'), self.tr('Cancel'), self)
            cancel_button.setIconSize(QSize(32, 32))
            self.addButton(cancel_button, QMessageBox.RejectRole)