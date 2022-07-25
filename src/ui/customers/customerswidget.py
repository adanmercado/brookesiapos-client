from PySide6.QtWidgets import QWidget

from .customerswidget_ui import CustomersWidget_UI

class CustomersWidget(CustomersWidget_UI, QWidget):
    def __init__(self, parent: QWidget) -> None:
        super(CustomersWidget, self).__init__(parent)
        self.setup()

    def setup(self):
        self.setupUi(self)