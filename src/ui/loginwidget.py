import os
from pathlib import Path

from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class LoginWidget(QWidget):
    def __init__(self):
        super(LoginWidget, self).__init__()
        self.setup()

    def setup(self):
        self.load_ui()

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle('Brookesia POS Login')

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / 'loginwidget.ui')
        ui_file = QFile(path)
        
        try:
            ui_file.open(QFile.ReadOnly)
            loader.load(ui_file, self)
        except:
            print(f'An error ocurred while uploading file {path}')
        finally:
            if ui_file.isOpen():
                ui_file.close()