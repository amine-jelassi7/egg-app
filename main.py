import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from interface import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonTwitter.clicked.connect(lambda : print("check my github for further informations"))
        self.ui.buttonFacebook.clicked.connect(lambda : print("check my github for further informations"))

        self.ui.pushButton.clicked.connect(self.boil)
        self.ui.titleLabel.setText("00:00")

    def boil(self):
        self.duration = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        if self.duration < 2400:
            sec = self.duration % 60
            min = self.duration // 60
            if min<2 :
                self.ui.imageLabel.setText('STILL RAW')
            elif min<4 :
                self.ui.imageLabel.setPixmap(QPixmap("D:\\egg app\\assets\\2mins.png"))
            elif min<6 :
                self.ui.imageLabel.setPixmap(QPixmap("D:\\egg app\\assets\\4mins.png"))
            elif min<8 :
                self.ui.imageLabel.setPixmap(QPixmap("D:\\egg app\\assets\\6mins.png"))
            elif min<12 :
                self.ui.imageLabel.setPixmap(QPixmap("D:\\egg app\\assets\\8mins.png"))
            elif min<14 :
                self.ui.imageLabel.setPixmap(QPixmap("D:\\egg app\\assets\\12mins.png"))
            else :
                self.ui.imageLabel.setPixmap(QPixmap("D:\\egg app\\assets\\flame.png"))
            self.ui.titleLabel.setText(f'{min:02}:{sec:02}')
            self.duration += 1
        else:
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
