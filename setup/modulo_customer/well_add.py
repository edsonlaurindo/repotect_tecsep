
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import modulo_customer.customer
import modulo_customer.custumerController
import modulo_wbco.wbcoController

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,user_name ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 850))

        desktop = QDesktopWidget()
        screenRect = desktop.screenGeometry()
        windowRect = MainWindow.geometry()

        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # Define a posição da janela
        MainWindow.move(x, y)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_aside_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_aside_menu.setGeometry(QtCore.QRect(0, -10, 251, 861))
        self.frame_aside_menu.setStyleSheet("\n" "background-color:#2f6d58")
        self.frame_aside_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_aside_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aside_menu.setObjectName("frame_aside_menu")
        self.label_15 = QtWidgets.QLabel(self.frame_aside_menu)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 221, 91))
        self.label_15.setStyleSheet("image: url(:/img/logo_tecsep-1-removebg-preview.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.btn_dashboard = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_dashboard.setGeometry(QtCore.QRect(30, 140, 191, 41))
        self.btn_dashboard.setStyleSheet("\n" "\n" "QPushButton#btn_dashboard{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_dashboard:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_dashboard:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/house-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QtCore.QSize(25, 25))
        self.btn_dashboard.setFlat(False)
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.btn_compliance = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_compliance.setGeometry(QtCore.QRect(30, 290, 191, 41))
        self.btn_compliance.setStyleSheet("QPushButton#btn_compliance{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "text-align:left;\n" "padding:10px\n" "}\n" "\n" "QPushButton#btn_compliance:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "}\n" "\n" "QPushButton#btn_compliance:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }\n" "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/vial-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_compliance.setIcon(icon1)
        self.btn_compliance.setIconSize(QtCore.QSize(25, 25))
        self.btn_compliance.setFlat(False)
        self.btn_compliance.setObjectName("btn_compliance")
        self.btn_wbco = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_wbco.setGeometry(QtCore.QRect(30, 340, 191, 41))
        self.btn_wbco.setStyleSheet("QPushButton#btn_wbco{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "text-align:left;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_wbco:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "}\n" "\n" "QPushButton#btn_wbco:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_wbco.setIcon(icon2)
        self.btn_wbco.setIconSize(QtCore.QSize(25, 25))
        self.btn_wbco.setFlat(False)
        self.btn_wbco.setObjectName("btn_wbco")
        self.btn_filtration = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_filtration.setGeometry(QtCore.QRect(30, 390, 191, 41))
        self.btn_filtration.setStyleSheet("QPushButton#btn_filtration{\n" "\n" "border:none;\n" "color:white;\n" "font-size:19px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "text-align:left;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_filtration:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "}\n" "\n" "QPushButton#btn_filtration:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/oil-well-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filtration.setIcon(icon3)
        self.btn_filtration.setIconSize(QtCore.QSize(25, 25))
        self.btn_filtration.setFlat(False)
        self.btn_filtration.setObjectName("btn_filtration")
        self.btn_tank_cleaning = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_tank_cleaning.setGeometry(QtCore.QRect(30, 440, 191, 41))
        self.btn_tank_cleaning.setStyleSheet("QPushButton#btn_tank_cleaning{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_tank_cleaning:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_tank_cleaning:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/soap-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tank_cleaning.setIcon(icon4)
        self.btn_tank_cleaning.setIconSize(QtCore.QSize(25, 25))
        self.btn_tank_cleaning.setFlat(False)
        self.btn_tank_cleaning.setObjectName("btn_tank_cleaning")
        self.btn_user_profile = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user_profile.setGeometry(QtCore.QRect(40, 710, 161, 41))
        self.btn_user_profile.setStyleSheet("QPushButton#btn_user_profile{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_user_profile:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_user_profile:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_user_profile.setIcon(icon5)
        self.btn_user_profile.setIconSize(QtCore.QSize(25, 25))
        self.btn_user_profile.setFlat(False)
        self.btn_user_profile.setObjectName("btn_user_profile")
        self.btn_logout = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_logout.setGeometry(QtCore.QRect(40, 760, 161, 41))
        self.btn_logout.setStyleSheet("QPushButton#btn_logout{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_logout:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_logout:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" " }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logout.setIcon(icon6)
        self.btn_logout.setIconSize(QtCore.QSize(25, 25))
        self.btn_logout.setFlat(False)
        self.btn_logout.setObjectName("btn_logout")


        self.btn_user = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user.setGeometry(QtCore.QRect(30, 190, 191, 41))
        self.btn_user.setStyleSheet("\n" "\n" "QPushButton#btn_user{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_user:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_user:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        self.btn_user.setIcon(icon5)
        self.btn_user.setIconSize(QtCore.QSize(25, 25))
        self.btn_user.setFlat(False)
        self.btn_user.setObjectName("btn_user")
        self.btn_customer = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_customer.setGeometry(QtCore.QRect(30, 240, 191, 41))
        self.btn_customer.setStyleSheet("\n" "\n" "QPushButton#btn_customer{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_customer:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_customer:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/user-group-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_customer.setIcon(icon7)
        self.btn_customer.setIconSize(QtCore.QSize(25, 25))
        self.btn_customer.setFlat(False)
        self.btn_customer.setObjectName("btn_customer")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 0, 1151, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(1151, 861))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 861))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:#eff2f9;\n" "\n" "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1151, 51))
        self.frame_2.setStyleSheet("background-color:#fff")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl_user_logado = QtWidgets.QLabel(self.frame_2)
        self.lbl_user_logado.setGeometry(QtCore.QRect(1020, 20, 111, 20))
        self.lbl_user_logado.setStyleSheet("")
        self.lbl_user_logado.setObjectName("lbl_user_logado")
        self.lbl_user_logado.setText(user_name)
        self.img_user_logado = QtWidgets.QPushButton(self.frame_2)
        self.img_user_logado.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.img_user_logado.setStyleSheet("background-color: #fff;\n" "border-radius:30px;\n" "width:30px;\n" "height:30px;")
        self.img_user_logado.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.img_user_logado.setIcon(icon8)
        self.img_user_logado.setIconSize(QtCore.QSize(25, 25))
        self.img_user_logado.setObjectName("img_user_logado")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 1151, 151))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(40, 50, 151, 31))
        self.label.setStyleSheet("font-size: 30px;\n" "color:#fff;")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n" "border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 431, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n""font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(-1, 830, 1151, 31))
        self.frame_9.setStyleSheet("background-color:#2d6b56;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(-40, 750, 41, 151))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);\n""border-color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(20, 270, 1091, 20))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);\n""")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btn_list_customer = QtWidgets.QPushButton(self.frame)
        self.btn_list_customer.setGeometry(QtCore.QRect(920, 240, 191, 31))
        self.btn_list_customer.setStyleSheet("\n" "\n" "QPushButton#btn_list_customer{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:14px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_list_customer:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_list_customer:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        self.btn_list_customer.setIcon(icon7)
        self.btn_list_customer.setObjectName("btn_list_customer")
        self.txt_nome = QtWidgets.QLineEdit(self.frame)
        self.txt_nome.setGeometry(QtCore.QRect(30, 390, 341, 41))
        self.txt_nome.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px;\n font-size:18px;" "}")
        self.txt_nome.setPlaceholderText("")
        self.txt_nome.setObjectName("txt_nome")
        self.lbl_nome = QtWidgets.QLabel(self.frame)
        self.lbl_nome.setGeometry(QtCore.QRect(30, 360, 81, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_nome.setFont(font)
        self.lbl_nome.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_nome.setObjectName("lbl_nome")
        self.txt_well_number = QtWidgets.QLineEdit(self.frame)
        self.txt_well_number.setGeometry(QtCore.QRect(390, 390, 341, 41))
        self.txt_well_number.setStyleSheet("QLineEdit{\n" "\n" "\n" "background-color:#fff;\n" "border: 1px solid #8ec0af;\n" "border-radius: 6px;\n font-size:18px;" "}")
        self.txt_well_number.setPlaceholderText("")
        self.txt_well_number.setObjectName("txt_well_number")
        self.cbx_customers = QtWidgets.QComboBox(self.frame)
        self.cbx_customers.setGeometry(QtCore.QRect(750, 390, 341, 41))
        self.cbx_customers.setPlaceholderText("")
        self.cbx_customers.setObjectName("cbx_customers")
        self.cbx_customers.setStyleSheet("""
            QComboBox {
                border: 1px solid #8ec0af;
                border-radius: 6px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
                background: white;
            }
            QComboBox:editable {
                background: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QComboBox::down-arrow {
                image: url(img/arrow_2.png);
            }
        """)

        self.lbl_number = QtWidgets.QLabel(self.frame)
        self.lbl_number.setGeometry(QtCore.QRect(390, 360, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_number.setFont(font)
        self.lbl_number.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_number.setObjectName("lbl_number")
        self.lbl_customers = QtWidgets.QLabel(self.frame)
        self.lbl_customers.setGeometry(QtCore.QRect(750, 360, 191, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        self.lbl_customers.setFont(font)
        self.lbl_customers.setStyleSheet("color: rgb(52, 52, 52);")
        self.lbl_customers.setObjectName("lbl_customers")
        
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        
        font = QtGui.QFont("Arial")
        font.setPointSize(11)
        
        self.btn_salvar_poco = QtWidgets.QPushButton(self.frame)
        self.btn_salvar_poco.setGeometry(QtCore.QRect(30, 490, 341, 41))
        self.btn_salvar_poco.setStyleSheet("\n" "\n" "QPushButton#btn_salvar_poco{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:16px;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_salvar_poco:hover{\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_salvar_poco:pressed {\n" " background-color: #044e42;\n" "border-radius: 6px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("..img/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_salvar_poco.setIcon(icon9)
        self.btn_salvar_poco.setIconSize(QtCore.QSize(25, 25))
        self.btn_salvar_poco.setObjectName("btn_salvar_poco")
        
        
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("/img/upload-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.lbl_customers.raise_()
        self.lbl_nome.raise_()
        self.lbl_number.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_9.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.btn_list_customer.raise_()
        self.txt_nome.raise_()
        self.txt_well_number.raise_()
        self.cbx_customers.raise_()
        self.btn_salvar_poco.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))

        self.btn_dashboard.setText(_translate("MainWindow", " Dashboard"))
        self.btn_dashboard.clicked.connect(lambda:show_form_dashboard())


        self.btn_compliance.setText(_translate("MainWindow", " A. M. Compliance"))
        self.btn_wbco.setText(_translate("MainWindow", " WBCO Tools"))
        self.btn_wbco.clicked.connect(lambda: call_form_wbco())
        self.btn_filtration.setText(_translate("MainWindow", " Filtration"))
        self.btn_tank_cleaning.setText(_translate("MainWindow", " Tank Cleaning"))
        self.btn_user_profile.setText(_translate("MainWindow", "User Profile"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_logout.clicked.connect(lambda:logout())

        self.btn_user.setText(_translate("MainWindow", " Personnel"))
        self.btn_user.clicked.connect(lambda:call_form_user())


        self.btn_customer.setText(_translate("MainWindow", "Customers"))
        self.label.setText(_translate("MainWindow", "Well"))
        self.label_2.setText(_translate("MainWindow", "Fill in all the fields to be able to add a new well to the system"))
        
        self.btn_list_customer.setText(_translate("MainWindow", "List Well"))
        self.btn_list_customer.clicked.connect(lambda:show_form_list_well())

        self.lbl_nome.setText(_translate("MainWindow", " Well Name"))
        self.lbl_number.setText(_translate("MainWindow", "Well Number"))
        self.lbl_customers.setText(_translate("MainWindow", "Customers"))
        

        self.btn_salvar_poco.setText(_translate("MainWindow", "Save Well data"))
        self.btn_salvar_poco.clicked.connect(lambda: save_data())
        
       


        def show_form_list_well():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.well
            self.ui = modulo_customer.well.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_dashboard():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.dashboard
            self.ui = modulo_home.dashboard.Ui_dashboard_ui()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def call_form_user():
            self.window = QtWidgets.QMainWindow()
            import modulo_personnel.personnel
            self.ui = modulo_personnel.personnel.form_personeel_list()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def call_form_wbco():
            self.window = QtWidgets.QMainWindow()
            import modulo_wbco.wbco
            self.ui = modulo_wbco.wbco.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def logout():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.login
            self.ui = modulo_home.login.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close()

        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Customer added successfully')
            msg_error.setWindowTitle('Adding Cusotmer')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        
        def carregar_cliente():
            self.cbx_customers.addItems(modulo_wbco.wbcoController.carregar_cliente())

        carregar_cliente()


        def save_data():
            customer_name = self.txt_nome.text()
            custumer = self.cbx_customers.currentText()
            well_number = self.txt_well_number.text()

            # Condicao para adicao de usuario
            if customer_name == "" or custumer == "" or well_number == "":
                msg_validation = QMessageBox()
                msg_validation.setIcon(QMessageBox.Critical)
                msg_validation.setText('Unsuccessful registration, existence of empty fields')
                msg_validation.setWindowTitle(' Error Adding Customer')
                msg_validation.exec_()
            else:
                import modulo_customer.custumerController
                id_cliente = modulo_wbco.wbcoController.carregar_buscar_id_cliente(self.cbx_customers.currentText())
                id_supervisor = modulo_wbco.wbcoController.carregar_id_supervisor_by_email(self.lbl_user_logado.text())
                modulo_customer.custumerController.carregar_cadastro_de_poco(customer_name,well_number,id_cliente,id_supervisor)

                self.txt_nome.clear()
                self.txt_well_number.clear()
                show_message_sucess()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
