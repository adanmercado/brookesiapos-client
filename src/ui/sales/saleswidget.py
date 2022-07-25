from PySide6.QtWidgets import QWidget, QListView

from .saleswidget_ui import SalesWidget_UI

class SalesWidget(SalesWidget_UI, QWidget):
    def __init__(self, parent: QWidget) -> None:
        super(SalesWidget, self).__init__(parent)
        self.setup()

    def setup(self):
        self.setupUi(self)

        self.customers_combobox.setView(QListView())

        with open('qrc/theme/default/saleswidget.qss', 'r') as qss:
            theme = qss.read()
            self.setStyleSheet(theme)