# Form implementation generated from reading ui file '.\UI\interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 416)
        MainWindow.setStyleSheet("*{\n"
"    background-color : transparent;\n"
"    margin : 0;\n"
"    padding : 0;\n"
"    border : none;\n"
"}\n"
"\n"
"#MainWindow{\n"
"    background-color : #DDDDDD;\n"
"}\n"
"\n"
"#menubar{\n"
"    background-color: #393E46;\n"
"    color : #EEEEEE;\n"
"}\n"
"\n"
"#menubar *{\n"
"    background-color: #393E46;\n"
"    color : #EEEEEE;\n"
"}\n"
"\n"
"#pBarPdf{\n"
"    background-color : #393E46;\n"
"    border-radius : 5px;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color : #DDDDDD;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color : white;\n"
"    background-color : #222831;\n"
"    padding : 5px 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color : white;\n"
"    background-color : #393E46;\n"
"    padding : 5px 15px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.home)
        self.pushButton.setStyleSheet("background-color : transparent;\n"
"border : none;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\logo/duncha.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(300, 300))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(parent=self.home)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stackedWidget.addWidget(self.home)
        self.gcode = QtWidgets.QWidget()
        self.gcode.setObjectName("gcode")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gcode)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleGCODE = QtWidgets.QLabel(parent=self.gcode)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleGCODE.setFont(font)
        self.titleGCODE.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleGCODE.setObjectName("titleGCODE")
        self.verticalLayout_3.addWidget(self.titleGCODE)
        self.topWidgetGcode = QtWidgets.QWidget(parent=self.gcode)
        self.topWidgetGcode.setObjectName("topWidgetGcode")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.topWidgetGcode)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.descLabelSourceGcode = QtWidgets.QLabel(parent=self.topWidgetGcode)
        self.descLabelSourceGcode.setObjectName("descLabelSourceGcode")
        self.verticalLayout_4.addWidget(self.descLabelSourceGcode)
        self.sourceGcode = QtWidgets.QWidget(parent=self.topWidgetGcode)
        self.sourceGcode.setObjectName("sourceGcode")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sourceGcode)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSourceGcode = QtWidgets.QPushButton(parent=self.sourceGcode)
        self.btnSourceGcode.setObjectName("btnSourceGcode")
        self.horizontalLayout.addWidget(self.btnSourceGcode)
        self.labelSourceGcode = QtWidgets.QLabel(parent=self.sourceGcode)
        self.labelSourceGcode.setObjectName("labelSourceGcode")
        self.horizontalLayout.addWidget(self.labelSourceGcode)
        self.verticalLayout_4.addWidget(self.sourceGcode)
        self.descLabelDestGcode = QtWidgets.QLabel(parent=self.topWidgetGcode)
        self.descLabelDestGcode.setObjectName("descLabelDestGcode")
        self.verticalLayout_4.addWidget(self.descLabelDestGcode)
        self.destGcode = QtWidgets.QWidget(parent=self.topWidgetGcode)
        self.destGcode.setObjectName("destGcode")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.destGcode)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnDestGcode = QtWidgets.QPushButton(parent=self.destGcode)
        self.btnDestGcode.setObjectName("btnDestGcode")
        self.horizontalLayout_2.addWidget(self.btnDestGcode)
        self.labelDestGcode = QtWidgets.QLabel(parent=self.destGcode)
        self.labelDestGcode.setObjectName("labelDestGcode")
        self.horizontalLayout_2.addWidget(self.labelDestGcode)
        self.verticalLayout_4.addWidget(self.destGcode)
        self.excelModeBox = QtWidgets.QCheckBox(parent=self.topWidgetGcode)
        self.excelModeBox.setObjectName("excelModeBox")
        self.verticalLayout_4.addWidget(self.excelModeBox)
        self.verticalLayout_3.addWidget(self.topWidgetGcode)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.bottomWidgetGcode = QtWidgets.QWidget(parent=self.gcode)
        self.bottomWidgetGcode.setObjectName("bottomWidgetGcode")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bottomWidgetGcode)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnCalcGcode = QtWidgets.QPushButton(parent=self.bottomWidgetGcode)
        self.btnCalcGcode.setObjectName("btnCalcGcode")
        self.horizontalLayout_3.addWidget(self.btnCalcGcode)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.bottomWidgetGcode)
        self.stackedWidget.addWidget(self.gcode)
        self.gcodeTuto = QtWidgets.QWidget()
        self.gcodeTuto.setObjectName("gcodeTuto")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gcodeTuto)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.etapeZeroGcode = QtWidgets.QLabel(parent=self.gcodeTuto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etapeZeroGcode.setFont(font)
        self.etapeZeroGcode.setObjectName("etapeZeroGcode")
        self.verticalLayout_2.addWidget(self.etapeZeroGcode)
        self.etapeUnGcode = QtWidgets.QLabel(parent=self.gcodeTuto)
        self.etapeUnGcode.setObjectName("etapeUnGcode")
        self.verticalLayout_2.addWidget(self.etapeUnGcode)
        self.etapeDeuxGcode = QtWidgets.QLabel(parent=self.gcodeTuto)
        self.etapeDeuxGcode.setObjectName("etapeDeuxGcode")
        self.verticalLayout_2.addWidget(self.etapeDeuxGcode)
        self.etapeTroisGcode = QtWidgets.QLabel(parent=self.gcodeTuto)
        self.etapeTroisGcode.setAcceptDrops(False)
        self.etapeTroisGcode.setWordWrap(True)
        self.etapeTroisGcode.setObjectName("etapeTroisGcode")
        self.verticalLayout_2.addWidget(self.etapeTroisGcode)
        self.etapeQuatreGcode = QtWidgets.QLabel(parent=self.gcodeTuto)
        self.etapeQuatreGcode.setWordWrap(True)
        self.etapeQuatreGcode.setObjectName("etapeQuatreGcode")
        self.verticalLayout_2.addWidget(self.etapeQuatreGcode)
        self.stackedWidget.addWidget(self.gcodeTuto)
        self.pdf = QtWidgets.QWidget()
        self.pdf.setObjectName("pdf")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pdf)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.titlePDF = QtWidgets.QLabel(parent=self.pdf)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titlePDF.setFont(font)
        self.titlePDF.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titlePDF.setObjectName("titlePDF")
        self.verticalLayout_6.addWidget(self.titlePDF)
        self.topWidgetPdf = QtWidgets.QWidget(parent=self.pdf)
        self.topWidgetPdf.setObjectName("topWidgetPdf")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.topWidgetPdf)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.descLabelSourcePdf = QtWidgets.QLabel(parent=self.topWidgetPdf)
        self.descLabelSourcePdf.setObjectName("descLabelSourcePdf")
        self.verticalLayout_5.addWidget(self.descLabelSourcePdf)
        self.sourcePdf = QtWidgets.QWidget(parent=self.topWidgetPdf)
        self.sourcePdf.setObjectName("sourcePdf")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.sourcePdf)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnSourcePdf = QtWidgets.QPushButton(parent=self.sourcePdf)
        self.btnSourcePdf.setObjectName("btnSourcePdf")
        self.horizontalLayout_5.addWidget(self.btnSourcePdf)
        self.labelSourcePdf = QtWidgets.QLabel(parent=self.sourcePdf)
        self.labelSourcePdf.setObjectName("labelSourcePdf")
        self.horizontalLayout_5.addWidget(self.labelSourcePdf)
        self.verticalLayout_5.addWidget(self.sourcePdf)
        self.descLabelDestPdf = QtWidgets.QLabel(parent=self.topWidgetPdf)
        self.descLabelDestPdf.setObjectName("descLabelDestPdf")
        self.verticalLayout_5.addWidget(self.descLabelDestPdf)
        self.destPdf = QtWidgets.QWidget(parent=self.topWidgetPdf)
        self.destPdf.setObjectName("destPdf")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.destPdf)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnDestPdf = QtWidgets.QPushButton(parent=self.destPdf)
        self.btnDestPdf.setObjectName("btnDestPdf")
        self.horizontalLayout_6.addWidget(self.btnDestPdf)
        self.labelDestPdf = QtWidgets.QLabel(parent=self.destPdf)
        self.labelDestPdf.setObjectName("labelDestPdf")
        self.horizontalLayout_6.addWidget(self.labelDestPdf)
        self.verticalLayout_5.addWidget(self.destPdf)
        self.verticalLayout_6.addWidget(self.topWidgetPdf)
        spacerItem3 = QtWidgets.QSpacerItem(20, 63, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.bottomWidgetPdf = QtWidgets.QWidget(parent=self.pdf)
        self.bottomWidgetPdf.setObjectName("bottomWidgetPdf")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bottomWidgetPdf)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btnCalcPdf = QtWidgets.QPushButton(parent=self.bottomWidgetPdf)
        self.btnCalcPdf.setObjectName("btnCalcPdf")
        self.horizontalLayout_4.addWidget(self.btnCalcPdf)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_6.addWidget(self.bottomWidgetPdf)
        self.pBarPdf = QtWidgets.QProgressBar(parent=self.pdf)
        self.pBarPdf.setProperty("value", 0)
        self.pBarPdf.setTextVisible(False)
        self.pBarPdf.setObjectName("pBarPdf")
        self.verticalLayout_6.addWidget(self.pBarPdf)
        self.stackedWidget.addWidget(self.pdf)
        self.pdfTuto = QtWidgets.QWidget()
        self.pdfTuto.setObjectName("pdfTuto")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pdfTuto)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.etapeZeroPdf = QtWidgets.QLabel(parent=self.pdfTuto)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etapeZeroPdf.setFont(font)
        self.etapeZeroPdf.setObjectName("etapeZeroPdf")
        self.verticalLayout_8.addWidget(self.etapeZeroPdf)
        self.etapeUnPdf = QtWidgets.QLabel(parent=self.pdfTuto)
        self.etapeUnPdf.setObjectName("etapeUnPdf")
        self.verticalLayout_8.addWidget(self.etapeUnPdf)
        self.etapeDeuxPdf = QtWidgets.QLabel(parent=self.pdfTuto)
        self.etapeDeuxPdf.setWordWrap(True)
        self.etapeDeuxPdf.setObjectName("etapeDeuxPdf")
        self.verticalLayout_8.addWidget(self.etapeDeuxPdf)
        self.etapeTroisPdf = QtWidgets.QLabel(parent=self.pdfTuto)
        self.etapeTroisPdf.setAcceptDrops(False)
        self.etapeTroisPdf.setWordWrap(True)
        self.etapeTroisPdf.setObjectName("etapeTroisPdf")
        self.verticalLayout_8.addWidget(self.etapeTroisPdf)
        self.etapeQuatrePdf = QtWidgets.QLabel(parent=self.pdfTuto)
        self.etapeQuatrePdf.setWordWrap(True)
        self.etapeQuatrePdf.setObjectName("etapeQuatrePdf")
        self.verticalLayout_8.addWidget(self.etapeQuatrePdf)
        self.stackedWidget.addWidget(self.pdfTuto)
        self.verticalLayout_7.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        self.menuGCODE = QtWidgets.QMenu(parent=self.menubar)
        self.menuGCODE.setObjectName("menuGCODE")
        self.menuPDF = QtWidgets.QMenu(parent=self.menubar)
        self.menuPDF.setObjectName("menuPDF")
        self.menuAccueil = QtWidgets.QMenu(parent=self.menubar)
        self.menuAccueil.setObjectName("menuAccueil")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCalculer = QtGui.QAction(parent=MainWindow)
        self.actionCalculer.setObjectName("actionCalculer")
        self.actionTutorielGcode = QtGui.QAction(parent=MainWindow)
        self.actionTutorielGcode.setObjectName("actionTutorielGcode")
        self.actionExtraire = QtGui.QAction(parent=MainWindow)
        self.actionExtraire.setObjectName("actionExtraire")
        self.actionTutorielPdf = QtGui.QAction(parent=MainWindow)
        self.actionTutorielPdf.setObjectName("actionTutorielPdf")
        self.actionAccueil = QtGui.QAction(parent=MainWindow)
        self.actionAccueil.setObjectName("actionAccueil")
        self.menuGCODE.addAction(self.actionCalculer)
        self.menuGCODE.addAction(self.actionTutorielGcode)
        self.menuPDF.addAction(self.actionExtraire)
        self.menuPDF.addAction(self.actionTutorielPdf)
        self.menuAccueil.addAction(self.actionAccueil)
        self.menubar.addAction(self.menuGCODE.menuAction())
        self.menubar.addAction(self.menuPDF.menuAction())
        self.menubar.addAction(self.menuAccueil.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Selectionnez une action dans la barre en haut a gauche"))
        self.titleGCODE.setText(_translate("MainWindow", "Estimateur code G"))
        self.descLabelSourceGcode.setText(_translate("MainWindow", "Choisir un fichier source :"))
        self.btnSourceGcode.setText(_translate("MainWindow", "Ouvrir ..."))
        self.labelSourceGcode.setText(_translate("MainWindow", "Choisir fichier ..."))
        self.descLabelDestGcode.setText(_translate("MainWindow", "Choisir un ficher de destination (.CSV)  :"))
        self.btnDestGcode.setText(_translate("MainWindow", "Engistrer sous ..."))
        self.labelDestGcode.setText(_translate("MainWindow", "Choisir destination ..."))
        self.excelModeBox.setText(_translate("MainWindow", "Excel Mode"))
        self.btnCalcGcode.setText(_translate("MainWindow", "Lancer éstimation"))
        self.etapeZeroGcode.setText(_translate("MainWindow", "Comment faire une estimation de temps ?"))
        self.etapeUnGcode.setText(_translate("MainWindow", "1 - Aller dans la barre de menu -> GCode -> Calculer."))
        self.etapeDeuxGcode.setText(_translate("MainWindow", "2 - Selectionnez votre fichier source, contenant tout le code G que vous souhaitez estimer."))
        self.etapeTroisGcode.setText(_translate("MainWindow", "3 - Selectionner le fichier de destination CSV. c\'est ce fichier Excel dans lequel seront enregistrée les estimation. Pour avoir plus de détails sur les conditions de coupes (si codées explicitement), cochez \"Excel Mode\""))
        self.etapeQuatreGcode.setText(_translate("MainWindow", "4 - Lancez l\'éstimation. Vous pouvez ensuite retrouver le fichier Excel au format CSV là où vous l\'avez enregistré."))
        self.titlePDF.setText(_translate("MainWindow", "Extracteur data PDF"))
        self.descLabelSourcePdf.setText(_translate("MainWindow", "Choisir les fichiers source :"))
        self.btnSourcePdf.setText(_translate("MainWindow", "Ouvrir ..."))
        self.labelSourcePdf.setText(_translate("MainWindow", "Choisir fichier ..."))
        self.descLabelDestPdf.setText(_translate("MainWindow", "Choisir un ficher de destination (.CSV) :"))
        self.btnDestPdf.setText(_translate("MainWindow", "Engistrer sous ..."))
        self.labelDestPdf.setText(_translate("MainWindow", "Choisir destination ..."))
        self.btnCalcPdf.setText(_translate("MainWindow", "Lancer extration"))
        self.etapeZeroPdf.setText(_translate("MainWindow", "Comment faire une extraction de data ?"))
        self.etapeUnPdf.setText(_translate("MainWindow", "1 - Aller dans la barre de menu ->PDF -> Extraire."))
        self.etapeDeuxPdf.setText(_translate("MainWindow", "2 - Selectionnez vos fichiesr pdf, utilisez CTRL + Click ou SHIFT + Click pour en selectionner plusieurs.."))
        self.etapeTroisPdf.setText(_translate("MainWindow", "3 - Selectionner le fichier de destination CSV. c\'est ce fichier Excel dans lequel seront enregistrée les données"))
        self.etapeQuatrePdf.setText(_translate("MainWindow", "4 - Lancez l\'extraction. Ce processus prend 3 à 4 secondes par fichier. Vous pouvez ensuite trouver les données dans le fichier Excel au format CSV là où vous l\'avez enregistré"))
        self.menuGCODE.setTitle(_translate("MainWindow", "GCODE"))
        self.menuPDF.setTitle(_translate("MainWindow", "PDF"))
        self.menuAccueil.setTitle(_translate("MainWindow", "Accueil"))
        self.actionCalculer.setText(_translate("MainWindow", "Calculer"))
        self.actionTutorielGcode.setText(_translate("MainWindow", "Tutoriel"))
        self.actionExtraire.setText(_translate("MainWindow", "Extraire"))
        self.actionTutorielPdf.setText(_translate("MainWindow", "Tutoriel"))
        self.actionAccueil.setText(_translate("MainWindow", "Accueil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
