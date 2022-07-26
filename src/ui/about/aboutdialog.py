from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtCore import Qt

from .aboutdialog_ui import AboutDialog_UI

LEGAL_INFO = '''
# Brookesia Point Of Sale

&nbsp;
&nbsp;

**Versión**  
1.0.0  

&nbsp;
&nbsp;

**Author**  
Adán Mercado  
_<adanmercado.dev@gmail.com>_  

&nbsp;
&nbsp;

**LICENSE**
'''

LICENSE_INFO = '''
MIT License

Copyright (c) 2022 Adán Mercado

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class AboutDialog(AboutDialog_UI, QDialog):
    def __init__(self, parent: QWidget) -> None:
        super(AboutDialog, self).__init__(parent)
        self.setup()

    def setup(self) -> None:
        self.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.tr('About Brookeisa POS'))
        self.setModal(True)

        self.info_label.setTextFormat(Qt.MarkdownText)
        self.info_label.setText(LEGAL_INFO)

        self.license_textedit.setPlainText(LICENSE_INFO)

        self.accept_button.clicked.connect(self.accept)