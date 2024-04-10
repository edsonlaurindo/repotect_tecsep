# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_mud_type.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from compliance.pack_mud_type import mud_typeController as controller


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 230)
        MainWindow.setMinimumSize(QtCore.QSize(700, 230))
        MainWindow.setMaximumSize(QtCore.QSize(700, 230))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1050, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(1050, 861))
        self.frame.setMaximumSize(QtCore.QSize(1050, 861))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:#fff;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1201, 51))
        self.frame_2.setStyleSheet("background-color:#fff")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.img_user_logado = QtWidgets.QPushButton(self.frame_2)
        self.img_user_logado.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.img_user_logado.setStyleSheet("background-color: #fff;\n"
"border-radius:30px;\n"
"width:30px;\n"
"height:30px;")
        self.img_user_logado.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../../../../../.designer/backup/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.img_user_logado.setIcon(icon)
        self.img_user_logado.setIconSize(QtCore.QSize(25, 25))
        self.img_user_logado.setObjectName("img_user_logado")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 20, 1201, 71))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbl_form_tittle = QtWidgets.QLabel(self.frame_3)
        self.lbl_form_tittle.setGeometry(QtCore.QRect(40, 0, 421, 41))
        self.lbl_form_tittle.setStyleSheet("font-size: 30px;\n"
"color:#fff;")
        self.lbl_form_tittle.setObjectName("lbl_form_tittle")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.lbl_form_text = QtWidgets.QLabel(self.frame_3)
        self.lbl_form_text.setGeometry(QtCore.QRect(40, 40, 511, 21))
        self.lbl_form_text.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.lbl_form_text.setObjectName("lbl_form_text")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(-1, 830, 1151, 31))
        self.frame_9.setStyleSheet("background-color:#2d6b56;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(-40, 750, 41, 151))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.lbl_syntetic_sg = QtWidgets.QLabel(self.frame)
        self.lbl_syntetic_sg.setGeometry(QtCore.QRect(10, 100, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_syntetic_sg.setFont(font)
        self.lbl_syntetic_sg.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_syntetic_sg.setObjectName("lbl_syntetic_sg")
        self.txt_description = QtWidgets.QLineEdit(self.frame)
        self.txt_description.setGeometry(QtCore.QRect(10, 130, 321, 41))
        self.txt_description.setStyleSheet("""
            QLineEdit {
                border: 1px solid #8ec0af;
                border-radius: 2px;
                padding: 5px;
                background-color: #fff;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #8ec0af;
                border-radius: 6px;
                min-width: 10em;
                padding: 6px;
            }
            QLineEdit:hover {
                border: 2px solid #bbb;
            }
            QLineEdit:enabled {
                background-color: white;
            }
            QLineEdit:disabled {
                background-color: #eee;
            }
            QLineEdit:read-only {
                background-color: #eee;
            }
            QLineEdit::placeholder {
                color: #ccc;
            }
        """)
        self.txt_description.setPlaceholderText("")
        self.txt_description.setObjectName("txt_description")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setGeometry(QtCore.QRect(360, 130, 321, 41))
        self.btn_save.setStyleSheet("\n"
"\n"
"QPushButton#btn_save{\n"
"\n"
"border:none;\n"
"background-color:#044e42;\n"
"color:white;\n"
"font-size:14px;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:rigth;\n"
"}\n"
"\n"
"QPushButton#btn_save:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_save:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../../../../../../img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setObjectName("btn_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Mud Type"))
        self.lbl_form_tittle.setText(_translate("MainWindow", "Mud Type / Base Oil type"))
        self.lbl_form_text.setText(_translate("MainWindow", "Fill in the fields to save a Mud Type / Base Oil type in system"))
        self.lbl_syntetic_sg.setText(_translate("MainWindow", "Description"))
        self.btn_save.setText(_translate("MainWindow", "Save data"))
        self.btn_save.clicked.connect(lambda:save_data())

        def show_message(title,message):
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Information)
             msg.setText(title)
             msg.setInformativeText(str(message))
             msg.setWindowTitle("Error")
             msg.exec_()

        def show_message_error(title,message):
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Critical)
             msg.setText(title)
             msg.setInformativeText(str(message))
             msg.setWindowTitle("Error")
             msg.exec_()


        def save_data():
            try:
                descricao = self.txt_description.text()
                salvar = controller.cadastrar(descricao)
                if salvar == 0:
                    show_message("Add","Data Saved")
                    MainWindow.close()
                else:
                    show_message_error("Add","Error saving data")
            except (TypeError,ValueError,Exception,) as e:
                print(f" Erro {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
