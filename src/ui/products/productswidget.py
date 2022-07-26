from PySide6.QtWidgets import QWidget

from .productswidget_ui import ProductsWidget_UI

class ProductsWidget(ProductsWidget_UI, QWidget):
    def __init__(self, parent: QWidget) -> None:
        super(ProductsWidget, self).__init__(parent)
        self.setup()

    def setup(self):
        self.setupUi(self)