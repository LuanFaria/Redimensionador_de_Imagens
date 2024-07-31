import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap



class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setStyleSheet(
            '* {background:  	#F0E68C}' ) # Formatação em CSS

        self.btn_redimensionar.setStyleSheet(
         '* {background: Chartreuse}'
        )

        self.btn_salvar.setStyleSheet(
         '* {background: tomato}'
        )

        self.btn_escolher.setStyleSheet(
            '* {background: Chartreuse}'
        )
        self.scrollArea.setStyleSheet(
            '* {background: black}'
        )

        self.scrollAreaWidgetContents.setStyleSheet(
            '*{background: white}'

        )
        self.input_abrir.setStyleSheet(
            '*{background: white; color:black}'

        )
        self.input_abrir.setStyleSheet(
            '*{background: white; color:black}'

        )

        self.altura.setStyleSheet(
            '*{background: white; color:black}'

        )
        self.largura.setStyleSheet(
            '*{background: white; color:black}'

        )

        self.btn_escolher.clicked.connect(self.abrir_imagem)
        self.btn_redimensionar.clicked.connect(self.redimensiona)
        self.btn_salvar.clicked.connect(self.salvar_imagem)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            '/home/luan/Imagens/',
            options=QFileDialog.DontUseNativeDialog # Para não Usar a caixa nativa do sistema operacional/
                                                    # funciona de qualquer jeito, com ou sem.
        )
        self.input_abrir.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.label_img.setPixmap(self.original_img)

        self.largura.setText(str(self.original_img.width()))
        self.altura.setText(str(self.original_img.height()))

    def redimensiona(self):
        largura = int(self.largura.text())
        self.nova_img = self.original_img.scaledToWidth(largura)
        self.label_img.setPixmap(self.nova_img)

        self.largura.setText(str(self.nova_img.width()))
        self.altura.setText(str(self.nova_img.height()))

    def salvar_imagem(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Abrir Imagem',
            '/home/luan/Imagens/',
            options=QFileDialog.DontUseNativeDialog # Para não Usar a caixa nativa do sistema operacional/
                                                    # funciona de qualquer jeito, com ou sem.
        )
        self.nova_img.save(imagem, 'PNG')
        #print('teste')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    rd = Redimensionar()
    rd.show()
    qt.exec_()
