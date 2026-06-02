import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 861)
        # Fixed typo: changed 'backrgound-color' to 'background-color'
        MainWindow.setStyleSheet("background-color:#000000;")
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # Fixed typo here as well
        self.centralwidget.setStyleSheet("background-color:#000000;\n")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.topBar = QtWidgets.QFrame(self.centralwidget)
        self.topBar.setStyleSheet("background-color: #1f1f1f; border-bottom: 2px solid #e94560;")
        self.topBar.setObjectName("topBar")
        self.horizontalLayout_topBar = QtWidgets.QHBoxLayout(self.topBar)
        self.horizontalLayout_topBar.setObjectName("horizontalLayout_topBar")
        self.labelLogo = QtWidgets.QLabel(self.topBar)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.labelLogo.setFont(font)
        self.labelLogo.setStyleSheet("font-weight: bold; font-size: 16px; color: #e94560;")
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout_topBar.addWidget(self.labelLogo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_topBar.addItem(spacerItem)
        self.buttonTwitter = QtWidgets.QPushButton(self.topBar)
        self.buttonTwitter.setStyleSheet("color: white; background-color: #444; padding: 5px 10px; border-radius: 5px;")
        self.buttonTwitter.setObjectName("buttonTwitter")
        self.horizontalLayout_topBar.addWidget(self.buttonTwitter)
        self.buttonFacebook = QtWidgets.QPushButton(self.topBar)
        self.buttonFacebook.setStyleSheet(
            "color: white; background-color: #444; padding: 5px 10px; border-radius: 5px;")
        self.buttonFacebook.setObjectName("buttonFacebook")
        self.horizontalLayout_topBar.addWidget(self.buttonFacebook)
        self.verticalLayout_main.addWidget(self.topBar)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 932, 780))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_content = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_content.setObjectName("verticalLayout_content")
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setStyleSheet("color: #ccc; padding: 10px; background-color: #2e2e2e; border: 1px dashed #555;")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_content.addWidget(self.imageLabel)
        self.titleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.titleLabel.setStyleSheet("font-size: 22px; font-weight: bold; color: #ffffff;background-color : #2e2e2e")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_content.addWidget(self.titleLabel)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(1000, 270))
        self.textEdit.setStyleSheet("background-color:#2e2e2e;\n"
                                    "color:#ffffff")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_content.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(
            "background-color: #e94560; color: white; padding: 8px 15px; border: none; border-radius: 4px;\n"
            "")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_content.addWidget(self.pushButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_main.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        # Dynamic window icon placement
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "assets", "2mins.png")
        if os.path.exists(icon_path):
            MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # FIX 1: Changed the window title here
        MainWindow.setWindowTitle(_translate("MainWindow", "Egg App By Amine"))

        self.labelLogo.setText(_translate("MainWindow", "Egg app By Amine"))
        self.buttonTwitter.setText(_translate("MainWindow", "Twitter"))
        self.buttonFacebook.setText(_translate("MainWindow", "Facebook"))
        self.imageLabel.setText(_translate("MainWindow", "[start to activate]"))

        # FIX 2: Fixed default template text to match the default timer setup
        self.titleLabel.setText(_translate("MainWindow", "00:00"))

        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; background-color:#2e2e2e;\">make sure to:</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; background-color:#2e2e2e;\">*have the water boiling before puting in the egg</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; background-color:#2e2e2e;\">*take the egg at a room temperature</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; background-color:#2e2e2e;\">*right after taking the egg out of the water cool it down to stop the cooking process</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Start cooking"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())