from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget,QMessageBox
import modulo_customer.custumerController

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,user_name):
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
        self.frame_aside_menu.setStyleSheet("\n"
"background-color:#2f6d58")
        self.frame_aside_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_aside_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aside_menu.setObjectName("frame_aside_menu")
        self.lbl_logo_tecseo = QtWidgets.QPushButton(self.frame_aside_menu)
        self.lbl_logo_tecseo.setGeometry(QtCore.QRect(1, 30, 240, 105))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/TECSEP_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lbl_logo_tecseo.setIcon(icon)
        self.lbl_logo_tecseo.setIconSize(QtCore.QSize(230, 230))
        self.lbl_logo_tecseo.setFlat(False)
        self.lbl_logo_tecseo.setStyleSheet("\n" "\n" "QPushButton#lbl_logo_tecseo{\n" "\n" "border:none;\n" "color:white;\n" "font-size:18px;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "text-align:left;\n" "}\n" "\n" "QPushButton#btn_dashboard:hover{\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "transition: background-color 0.5s ease;\n" "padding:10px;\n" "}\n" "\n" "QPushButton#btn_dashboard:pressed {\n" " background-color: #044e42;\n" "border-radius: 12px;\n" "background-color: #033029;\n" "padding:10px;\n" " }\n" "\n" "\n" "")
        self.lbl_logo_tecseo.setObjectName("lbl_logo_tecseo")
        self.btn_dashboard = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_dashboard.setGeometry(QtCore.QRect(30, 140, 191, 41))
        self.btn_dashboard.setStyleSheet("\n"
"\n"
"QPushButton#btn_dashboard{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_dashboard:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_dashboard:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/house-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon_edit = QtGui.QIcon()
        icon_edit.addPixmap(QtGui.QPixmap("img/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        icon_delete = QtGui.QIcon()
        icon_delete.addPixmap(QtGui.QPixmap("img/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QtCore.QSize(25, 25))
        self.btn_dashboard.setFlat(False)
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.btn_compliance = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_compliance.setGeometry(QtCore.QRect(30, 290, 191, 41))
        self.btn_compliance.setStyleSheet("QPushButton#btn_compliance{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"text-align:left;\n"
"padding:10px\n"
"}\n"
"\n"
"QPushButton#btn_compliance:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QPushButton#btn_compliance:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/vial-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_compliance.setIcon(icon1)
        self.btn_compliance.setIconSize(QtCore.QSize(25, 25))
        self.btn_compliance.setFlat(False)
        self.btn_compliance.setObjectName("btn_compliance")
        self.btn_wbco = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_wbco.setGeometry(QtCore.QRect(30, 340, 191, 41))
        self.btn_wbco.setStyleSheet("QPushButton#btn_wbco{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"text-align:left;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_wbco:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QPushButton#btn_wbco:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_wbco.setIcon(icon2)
        self.btn_wbco.setIconSize(QtCore.QSize(25, 25))
        self.btn_wbco.setFlat(False)
        self.btn_wbco.setObjectName("btn_wbco")
        self.btn_filtration = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_filtration.setGeometry(QtCore.QRect(30, 390, 191, 41))
        self.btn_filtration.setStyleSheet("QPushButton#btn_filtration{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:19px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"text-align:left;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_filtration:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QPushButton#btn_filtration:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/oil-well-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filtration.setIcon(icon3)
        self.btn_filtration.setIconSize(QtCore.QSize(25, 25))
        self.btn_filtration.setFlat(False)
        self.btn_filtration.setObjectName("btn_filtration")
        self.btn_tank_cleaning = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_tank_cleaning.setGeometry(QtCore.QRect(30, 440, 191, 41))
        self.btn_tank_cleaning.setStyleSheet("QPushButton#btn_tank_cleaning{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_tank_cleaning:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_tank_cleaning:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/soap-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tank_cleaning.setIcon(icon4)
        self.btn_tank_cleaning.setIconSize(QtCore.QSize(25, 25))
        self.btn_tank_cleaning.setFlat(False)
        self.btn_tank_cleaning.setObjectName("btn_tank_cleaning")
        self.btn_user_profile = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user_profile.setGeometry(QtCore.QRect(40, 710, 161, 41))
        self.btn_user_profile.setStyleSheet("QPushButton#btn_user_profile{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_user_profile:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_user_profile:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_user_profile.setIcon(icon5)
        self.btn_user_profile.setIconSize(QtCore.QSize(25, 25))
        self.btn_user_profile.setFlat(False)
        self.btn_user_profile.setObjectName("btn_user_profile")
        self.btn_logout = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_logout.setGeometry(QtCore.QRect(40, 760, 161, 41))
        self.btn_logout.setStyleSheet("QPushButton#btn_logout{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_logout:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_logout:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
" }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/right-from-bracket-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logout.setIcon(icon6)
        self.btn_logout.setIconSize(QtCore.QSize(25, 25))
        self.btn_logout.setFlat(False)
        self.btn_logout.setObjectName("btn_logout")
        self.btn_user = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_user.setGeometry(QtCore.QRect(30, 190, 191, 41))
        self.btn_user.setStyleSheet("\n"
"\n"
"QPushButton#btn_user{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_user:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_user:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"\n"
"\n"
"")
        self.btn_user.setIcon(icon5)
        self.btn_user.setIconSize(QtCore.QSize(25, 25))
        self.btn_user.setFlat(False)
        self.btn_user.setObjectName("btn_user")
        self.btn_customer = QtWidgets.QPushButton(self.frame_aside_menu)
        self.btn_customer.setGeometry(QtCore.QRect(30, 240, 191, 41))
        self.btn_customer.setStyleSheet("\n"
"\n"
"QPushButton#btn_customer{\n"
"\n"
"border:none;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"text-align:left;\n"
"}\n"
"\n"
"QPushButton#btn_customer:hover{\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_customer:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 12px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"\n"
"\n"
"")
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
        self.frame.setStyleSheet("background-color:#fff;\n"
"\n"
"")
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
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.pushButton_5.setStyleSheet("background-color: #fff;\n"
"border-radius:30px;\n"
"width:30px;\n"
"height:30px;")
        self.pushButton_5.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/user_dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 1151, 151))
        self.frame_3.setStyleSheet("background-color:#2d6b56;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_titulo_form = QtWidgets.QLabel(self.frame_3)
        self.label_titulo_form.setGeometry(QtCore.QRect(40, 50, 151, 31))
        self.label_titulo_form.setStyleSheet("font-size: 30px;\n"
"color:#fff;")
        self.label_titulo_form.setObjectName("label_titulo_form")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(-10, 0, 21, 151))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.lbl_text_form = QtWidgets.QLabel(self.frame_3)
        self.lbl_text_form.setGeometry(QtCore.QRect(40, 90, 431, 16))
        self.lbl_text_form.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.lbl_text_form.setObjectName("lbl_text_form")
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
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(20, 270, 1091, 20))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btn_add_customer = QtWidgets.QPushButton(self.frame)
        self.btn_add_customer.setGeometry(QtCore.QRect(920, 240, 191, 31))
        self.btn_add_customer.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_customer{\n"
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
"QPushButton#btn_add_customer:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_customer:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_customer.setIcon(icon7)
        self.btn_add_customer.setObjectName("btn_add_customer")



        #Botão de Listagem de Poco


        self.btn_list_well = QtWidgets.QPushButton(self.frame)
        self.btn_list_well.setGeometry(QtCore.QRect(520, 240, 191, 31))
        self.btn_list_well.setStyleSheet("\n"
"\n"
"QPushButton#btn_list_well{\n"
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
"QPushButton#btn_list_well:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_list_well:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_list_well.setIcon(icon7)
        self.btn_list_well.setObjectName("btn_list_well")


        # Botao Adicionar Poco

        self.btn_add_well = QtWidgets.QPushButton(self.frame)
        self.btn_add_well.setGeometry(QtCore.QRect(720, 240,191,31))
        self.btn_add_well.setStyleSheet("\n"
"\n"
"QPushButton#btn_add_well{\n"
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
"QPushButton#btn_add_well:hover{\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"transition: background-color 0.5s ease;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton#btn_add_well:pressed {\n"
" background-color: #044e42;\n"
"border-radius: 6px;\n"
"background-color: #033029;\n"
"padding:10px;\n"
" }\n"
"")
        self.btn_add_well.setIcon(icon7)
        self.btn_add_well.setObjectName("btn_add_well")

        

        self.table_customer = QtWidgets.QTableWidget(self.frame)
        self.table_customer.setGeometry(QtCore.QRect(20, 320, 1091, 421))
        self.table_customer.setAutoFillBackground(True)
        self.table_customer.setStyleSheet("QTableWidget{\n"
"\n"
"\n"
"border:none;\n"
"selection-color:green;\n"
"selection-background-color:red;\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"color:white;\n"
"background-color:#044e42;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"\n"
"background-color:#044e42;\n"
"color:#fff;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"}\n"
"QTableWidget::item{ padding:1px;}"
"\n"
"\n"
"\n"
"")
        self.table_customer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_customer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_customer.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_customer.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_customer.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_customer.setShowGrid(False)
        self.table_customer.setGridStyle(QtCore.Qt.NoPen)
        self.table_customer.setCornerButtonEnabled(False)
        self.table_customer.setObjectName("table_customer")
        self.table_customer.setColumnCount(7)
        self.table_customer.setHorizontalHeaderLabels(["Name","Nif","E-mail","Contact","Address","",""])
        self.table_customer.horizontalHeaderItem(0).setTextAlignment(0x0001)
        self.table_customer.horizontalHeaderItem(1).setTextAlignment(0x0001)
        self.table_customer.horizontalHeaderItem(2).setTextAlignment(0x0001)
        self.table_customer.horizontalHeaderItem(3).setTextAlignment(0x0001)
        self.table_customer.horizontalHeaderItem(4).setTextAlignment(0x0001)
        self.table_customer.horizontalHeaderItem(5).setTextAlignment(0x0001)
        self.table_customer.horizontalHeaderItem(6).setTextAlignment(0x0001)
        list_cliente = modulo_customer.custumerController.listar()
        self.table_customer.setRowCount(10)
        tablerow = 0

        for row in list_cliente:
            
            self.btn_edit_customer = QtWidgets.QPushButton("Edit Customer")
            self.btn_edit_customer.setStyleSheet("\n" "\n" "QPushButton#btn_edit_customer{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:13px;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_edit_customer:hover{\n" " background-color: #044e42;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "}\n" "\n" "QPushButton#btn_edit_customer:pressed {\n" " background-color: #044e42;\n" "border-radius: 0px;\n" "background-color: #033029;\n" "padding:5px;\n" " }\n" "")
            self.btn_edit_customer.setIcon(icon_edit)
            self.btn_edit_customer.setObjectName("btn_edit_customer")

            self.btn_remove_customer = QtWidgets.QPushButton("Remove Cuastomer")
            self.btn_remove_customer.setStyleSheet("\n" "\n" "QPushButton#btn_remove_customer{\n" "\n" "border:none;\n" "background-color:#044e42;\n" "color:white;\n" "font-size:13px;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "text-align:rigth;\n" "}\n" "\n" "QPushButton#btn_remove_customer:hover{\n" " background-color: #044e42;\n" "border-radius: 3px;\n" "transition: background-color 0.5s ease;\n" "padding:5px;\n" "}\n" "\n" "QPushButton#btn_remove_customer:pressed {\n" " background-color: #044e42;\n" "border-radius: 0px;\n" "background-color: #033029;\n" "padding:5px;\n" " }\n" "")
            self.btn_remove_customer.setIcon(icon_delete)
            self.btn_remove_customer.setObjectName("btn_remove_customer")

            self.table_customer.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[2]))
            self.table_customer.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_customer.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.table_customer.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.table_customer.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[6]))
            self.table_customer.setCellWidget(tablerow,5, self.btn_edit_customer)
            self.table_customer.setCellWidget(tablerow,6, self.btn_remove_customer)

            self.btn_edit_customer.clicked.connect(lambda:btn_clicked_edit())
            self.btn_remove_customer.clicked.connect(lambda:btn_clicked_delete())

            tablerow+=1

        def show_message_sucess():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Information)
            msg_error.setText('Customer successfully removed')
            msg_error.setWindowTitle('Custimer removal')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def show_message_error():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText('Error removing Customer')
            msg_error.setWindowTitle('Customer removal')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/sucess_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_error.setWindowIcon(icon)
            msg_error.exec_()

        def call_form_client():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer
            self.ui = modulo_customer.customer.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_edit_customer(nome,nif,email,contacto, adress):
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer_edit
            self.ui = modulo_customer.customer_edit.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text(),nome,nif,email,contacto,adress)
            self.window.show()
            MainWindow.close()
        
        def btn_clicked_edit():
            self.btn_edit_customer = self.btn_edit_customer.sender()
            if isinstance(self.btn_edit_customer, QtWidgets.QPushButton):
                index = self.table_customer.indexAt(self.btn_edit_customer.pos())
                row = index.row()
                col = index.column()


                col_nif = col - 4
                col_email = col - 3
                col_contacto = col - 2
                col_adress = col - 1
                col = col - 5
                

        

               
                

                item_nif = self.table_customer.item(row,col_nif)
                item = self.table_customer.item(row,col)
                item_email = self.table_customer.item(row,col_email)
                item_contacto = self.table_customer.item(row,col_contacto)
                item_adress = self.table_customer.item(row, col_adress)
                
                if item is not None:
                    
                    cliente = item.text()
                    nif = item_nif.text()
                    email = item_email.text()
                    contacto = item_contacto.text()
                    adress = item_adress.text()
                    show_form_edit_customer(cliente,nif,email,contacto,adress)

        
        def btn_clicked_delete(): 
            self.btn_remove_customer = self.btn_remove_customer.sender()
            if isinstance(self.btn_remove_customer, QtWidgets.QPushButton):

                index = self.table_customer.indexAt(self.btn_remove_customer.pos())
                row = index.row()
                col = index.column()
 
                #Pegar a coluna Nif
                col_nif = col - 5
                
                item = self.table_customer.item(row,col_nif)
                if item is not None:
                    
                    nif = item.text()
                    print(nif)
                    response = modulo_customer.custumerController.eliminar(nif)  
                    if response == 0:
                        show_message_sucess()
                        call_form_client()
                    else:
                        show_message_error()
                
                    
                    

        self.table_customer.horizontalHeader().setDefaultSectionSize(217)
        self.table_customer.horizontalHeader().setHighlightSections(False)
        self.table_customer.verticalHeader().setVisible(False)
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
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
        self.btn_filtration.setText(_translate("MainWindow", " Filtration"))
        self.btn_tank_cleaning.setText(_translate("MainWindow", " Tank Cleaning"))
        self.btn_user_profile.setText(_translate("MainWindow", "User Profile"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_logout.clicked.connect(lambda:logout())

        self.btn_user.setText(_translate("MainWindow", " Personnel"))

        self.btn_customer.setText(_translate("MainWindow", "Customers"))
        self.label_titulo_form.setText(_translate("MainWindow", "Customer"))
        self.lbl_text_form.setText(_translate("MainWindow", "Below is the list of all customers registered in the system"))
       
        self.btn_add_customer.setText(_translate("MainWindow", "Add new Customer"))
        self.btn_add_customer.clicked.connect(lambda: show_form_add_customer())
       
        self.btn_add_well.setText(_translate("MainWindow","Add new Well"))
        self.btn_add_well.clicked.connect(lambda:show_form_add_well())

        self.btn_list_well.setText(_translate("MainWindow","List Well"))
        self.btn_list_well.clicked.connect(lambda:show_form_list_well())

        self.btn_compliance.clicked.connect(lambda:show_form_compliance())
        self.btn_wbco.clicked.connect(lambda:call_form_wbco())
        self.btn_logout.clicked.connect(lambda: logout())
        self.btn_customer.clicked.connect(lambda: call_form_client())
        self.btn_filtration.clicked.connect(lambda:show_add_filtration())
        self.btn_tank_cleaning.clicked.connect(lambda:show_add_tank_cleaning())
        self.btn_user_profile.clicked.connect(lambda:show_perfil_user())


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

        def show_form_add_customer():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer_add
            self.ui = modulo_customer.customer_add.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_add_well():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.well_add
            self.ui = modulo_customer.well_add.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def call_form_client():
            self.window = QtWidgets.QMainWindow()
            import modulo_customer.customer
            self.ui = modulo_customer.customer.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_form_compliance():
            self.window = QtWidgets.QMainWindow()
            import  compliance.compliance_view as list
            self.ui = list.Ui_MainWindow()
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

        def show_add_filtration():
            self.window = QtWidgets.QMainWindow()
            import  filtration.filtration
            self.ui = filtration.filtration.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()  

        def show_add_tank_cleaning():
            self.window = QtWidgets.QMainWindow()
            import  tank_cleanning.tank_cleaning_view
            self.ui = tank_cleanning.tank_cleaning_view.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()
            MainWindow.close()

        def show_perfil_user():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.user_profile as user
            self.ui = user.Ui_MainWindow()
            self.ui.setupUi(self.window,self.lbl_user_logado.text())
            self.window.show()      
        
        def logout():
            self.window = QtWidgets.QMainWindow()
            import modulo_home.login
            self.ui = modulo_home.login.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close()

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
