# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'practicaExeYCFjcJ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(233, 314)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(1000, 1000))
        icon = QIcon()
        icon.addFile(u":/images/imagenes/Animals.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 230, 141, 61))
        self.pushButton.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(170, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/images/imagenes/exit-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(60, 60))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 190, 113, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"color: rgb(5, 5, 5);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 140, 91, 41))
        self.label.setStyleSheet(u"background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 255, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 161, 111))
        self.label_2.setStyleSheet(u"alternate-background-color: rgb(255, 170, 0);\n"
"background-color: rgb(0, 170, 255);")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setPixmap(QPixmap(u":/images/imagenes/facebook-480.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        self.lineEdit.textChanged.connect(self.label.setText)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Ejemplo", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Bot\u00f3n", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Entrada", None))
        self.label.setText(QCoreApplication.translate("Form", u"Etiqueta", None))
        self.label_2.setText("")
    # retranslateUi
import rc_images

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
