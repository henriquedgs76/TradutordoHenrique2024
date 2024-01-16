import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QSizePolicy, QComboBox, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QMimeData
from googletrans import Translator

class TradutorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tradutor do HENRIQUE 2024')
        self.setGeometry(300, 300, 600, 300)

        self.setup_ui()

    def setup_ui(self):
        self.setFonts()

        self.titulo = self.createLabel('Sistema de Tradução do Henrique 2024', is_title=True, font_size=30)
        self.label_original, self.texto_original = self.createInputPair('Texto Original:')
        self.label_idioma_destino, self.combo_idiomas = self.createLanguageSelector()
        self.label_traduzido, self.texto_traduzido = self.createOutputPair('Texto Traduzido:')
        
        self.botao_traduzir = self.createTranslateButton()
        self.botao_copiar = self.createCopyButton()

        layout_vertical = QVBoxLayout()

        layout_vertical.addWidget(self.titulo, alignment=Qt.AlignCenter)
        layout_vertical.addWidget(self.label_original)
        layout_vertical.addWidget(self.texto_original)
        layout_vertical.addWidget(self.createSeparator())
        layout_vertical.addWidget(self.label_idioma_destino)
        layout_vertical.addWidget(self.combo_idiomas)
        layout_vertical.addWidget(self.createSeparator())
        layout_vertical.addWidget(self.label_traduzido)
        layout_vertical.addWidget(self.texto_traduzido)
        layout_vertical.addWidget(self.botao_traduzir, alignment=Qt.AlignCenter)
        layout_vertical.addWidget(self.botao_copiar, alignment=Qt.AlignCenter)

        self.setLayout(layout_vertical)

    def setFonts(self):
        self.font_titulo = QFont("Arial", 16, QFont.Bold)
        self.font_label = QFont("Arial", 12)

    def createLabel(self, text, is_title=False, font_size=None):
        label = QLabel(text, self)
        if is_title:
            label.setFont(QFont("Arial", font_size, QFont.Bold))
        else:
            label.setFont(QFont("Arial", self.font_label.pointSize()) if font_size else self.font_label)
        label.setAlignment(Qt.AlignCenter if is_title else Qt.AlignLeft)
        return label

    def createInputPair(self, label_text, enabled=True):
        label = self.createLabel(label_text)
        text_input = QLineEdit(self)
        text_input.setEnabled(enabled)
        return label, text_input

    def createOutputPair(self, label_text, enabled=True):
        label = self.createLabel(label_text)
        text_output = QTextEdit(self)
        text_output.setReadOnly(True)
        text_output.setEnabled(enabled)
        return label, text_output

    def createLanguageSelector(self):
        label = self.createLabel('Idioma de Destino:')
        combo_box = QComboBox(self)
        
        
        idiomas = {
            'Inglês': 'en',
            'Espanhol': 'es',
            'Mandarim': 'zh-CN',
            'Hindi': 'hi',
            'Árabe': 'ar',
            'Bengali': 'bn',
            'Português': 'pt',
            'Russo': 'ru',
            'Urdu': 'ur',
            'Indonésio': 'id',
        }

        
        combo_box.addItems(idiomas.keys())
        combo_box.setInsertPolicy(QComboBox.InsertAtTop)

        return label, combo_box

    def createTranslateButton(self):
        button = QPushButton('Traduzir', self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("background-color: #4CAF50; color: white;")
        button.clicked.connect(self.traduzir_texto)
        return button

    def createCopyButton(self):
        button = QPushButton('Copiar', self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("background-color: #008CBA; color: white;")
        button.clicked.connect(self.copiar_texto)
        return button

    def createSeparator(self):
        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        return separator

    def traduzir_texto(self):
        texto_original = self.texto_original.text()
        idioma_destino_nome = self.combo_idiomas.currentText()
        idiomas = {
            'Inglês': 'en',
            'Espanhol': 'es',
            'Mandarim': 'zh-CN',
            'Hindi': 'hi',
            'Árabe': 'ar',
            'Bengali': 'bn',
            'Português': 'pt',
            'Russo': 'ru',
            'Urdu': 'ur',
            'Indonésio': 'id',
        }
        idioma_destino = idiomas.get(idioma_destino_nome)

        tradutor = Translator()
        resultado = tradutor.translate(texto_original, dest=idioma_destino)
        texto_traduzido = resultado.text

        self.texto_traduzido.setPlainText(texto_traduzido)

    def copiar_texto(self):
        texto_traduzido = self.texto_traduzido.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(texto_traduzido, mode=clipboard.Clipboard)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tradutor_app = TradutorApp()
    tradutor_app.show()
    sys.exit(app.exec_())
