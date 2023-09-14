# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(514, 406)
        self.actionCalculer = QAction(MainWindow)
        self.actionCalculer.setObjectName(u"actionCalculer")
        self.actionTutorielGcode = QAction(MainWindow)
        self.actionTutorielGcode.setObjectName(u"actionTutorielGcode")
        self.actionExtraire = QAction(MainWindow)
        self.actionExtraire.setObjectName(u"actionExtraire")
        self.actionTutorielPdf = QAction(MainWindow)
        self.actionTutorielPdf.setObjectName(u"actionTutorielPdf")
        self.actionAccueil = QAction(MainWindow)
        self.actionAccueil.setObjectName(u"actionAccueil")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout = QVBoxLayout(self.home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.home)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color : transparent;\n"
"border : none;")
        icon = QIcon()
        icon.addFile(u"logo/duncha.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(300, 300))

        self.verticalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.stackedWidget.addWidget(self.home)
        self.gcode = QWidget()
        self.gcode.setObjectName(u"gcode")
        self.verticalLayout_3 = QVBoxLayout(self.gcode)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titleGCODE = QLabel(self.gcode)
        self.titleGCODE.setObjectName(u"titleGCODE")
        font1 = QFont()
        font1.setPointSize(20)
        self.titleGCODE.setFont(font1)
        self.titleGCODE.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.titleGCODE)

        self.topWidgetGcode = QWidget(self.gcode)
        self.topWidgetGcode.setObjectName(u"topWidgetGcode")
        self.verticalLayout_4 = QVBoxLayout(self.topWidgetGcode)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.descLabelSourceGcode = QLabel(self.topWidgetGcode)
        self.descLabelSourceGcode.setObjectName(u"descLabelSourceGcode")

        self.verticalLayout_4.addWidget(self.descLabelSourceGcode)

        self.sourceGcode = QWidget(self.topWidgetGcode)
        self.sourceGcode.setObjectName(u"sourceGcode")
        self.horizontalLayout = QHBoxLayout(self.sourceGcode)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSourceGcode = QPushButton(self.sourceGcode)
        self.btnSourceGcode.setObjectName(u"btnSourceGcode")

        self.horizontalLayout.addWidget(self.btnSourceGcode)

        self.labelSourceGcode = QLabel(self.sourceGcode)
        self.labelSourceGcode.setObjectName(u"labelSourceGcode")

        self.horizontalLayout.addWidget(self.labelSourceGcode)


        self.verticalLayout_4.addWidget(self.sourceGcode)

        self.descLabelDestGcode = QLabel(self.topWidgetGcode)
        self.descLabelDestGcode.setObjectName(u"descLabelDestGcode")

        self.verticalLayout_4.addWidget(self.descLabelDestGcode)

        self.destGcode = QWidget(self.topWidgetGcode)
        self.destGcode.setObjectName(u"destGcode")
        self.horizontalLayout_2 = QHBoxLayout(self.destGcode)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnDestGcode = QPushButton(self.destGcode)
        self.btnDestGcode.setObjectName(u"btnDestGcode")

        self.horizontalLayout_2.addWidget(self.btnDestGcode)

        self.labelDestGcode = QLabel(self.destGcode)
        self.labelDestGcode.setObjectName(u"labelDestGcode")

        self.horizontalLayout_2.addWidget(self.labelDestGcode)


        self.verticalLayout_4.addWidget(self.destGcode)


        self.verticalLayout_3.addWidget(self.topWidgetGcode)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.bottomWidgetGcode = QWidget(self.gcode)
        self.bottomWidgetGcode.setObjectName(u"bottomWidgetGcode")
        self.horizontalLayout_3 = QHBoxLayout(self.bottomWidgetGcode)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnCalcGcode = QPushButton(self.bottomWidgetGcode)
        self.btnCalcGcode.setObjectName(u"btnCalcGcode")

        self.horizontalLayout_3.addWidget(self.btnCalcGcode)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.bottomWidgetGcode)

        self.stackedWidget.addWidget(self.gcode)
        self.gcodeTuto = QWidget()
        self.gcodeTuto.setObjectName(u"gcodeTuto")
        self.verticalLayout_2 = QVBoxLayout(self.gcodeTuto)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.etapeZeroGcode = QLabel(self.gcodeTuto)
        self.etapeZeroGcode.setObjectName(u"etapeZeroGcode")
        font2 = QFont()
        font2.setPointSize(12)
        self.etapeZeroGcode.setFont(font2)

        self.verticalLayout_2.addWidget(self.etapeZeroGcode)

        self.etapeUnGcode = QLabel(self.gcodeTuto)
        self.etapeUnGcode.setObjectName(u"etapeUnGcode")

        self.verticalLayout_2.addWidget(self.etapeUnGcode)

        self.etapeDeuxGcode = QLabel(self.gcodeTuto)
        self.etapeDeuxGcode.setObjectName(u"etapeDeuxGcode")

        self.verticalLayout_2.addWidget(self.etapeDeuxGcode)

        self.etapeTroisGcode = QLabel(self.gcodeTuto)
        self.etapeTroisGcode.setObjectName(u"etapeTroisGcode")
        self.etapeTroisGcode.setAcceptDrops(False)
        self.etapeTroisGcode.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.etapeTroisGcode)

        self.etapeQuatreGcode = QLabel(self.gcodeTuto)
        self.etapeQuatreGcode.setObjectName(u"etapeQuatreGcode")
        self.etapeQuatreGcode.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.etapeQuatreGcode)

        self.stackedWidget.addWidget(self.gcodeTuto)
        self.pdf = QWidget()
        self.pdf.setObjectName(u"pdf")
        self.verticalLayout_6 = QVBoxLayout(self.pdf)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.titlePDF = QLabel(self.pdf)
        self.titlePDF.setObjectName(u"titlePDF")
        self.titlePDF.setFont(font1)
        self.titlePDF.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.titlePDF)

        self.topWidgetPdf = QWidget(self.pdf)
        self.topWidgetPdf.setObjectName(u"topWidgetPdf")
        self.verticalLayout_5 = QVBoxLayout(self.topWidgetPdf)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.descLabelSourcePdf = QLabel(self.topWidgetPdf)
        self.descLabelSourcePdf.setObjectName(u"descLabelSourcePdf")

        self.verticalLayout_5.addWidget(self.descLabelSourcePdf)

        self.sourcePdf = QWidget(self.topWidgetPdf)
        self.sourcePdf.setObjectName(u"sourcePdf")
        self.horizontalLayout_5 = QHBoxLayout(self.sourcePdf)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnSourcePdf = QPushButton(self.sourcePdf)
        self.btnSourcePdf.setObjectName(u"btnSourcePdf")

        self.horizontalLayout_5.addWidget(self.btnSourcePdf)

        self.labelSourcePdf = QLabel(self.sourcePdf)
        self.labelSourcePdf.setObjectName(u"labelSourcePdf")

        self.horizontalLayout_5.addWidget(self.labelSourcePdf)


        self.verticalLayout_5.addWidget(self.sourcePdf)

        self.descLabelDestPdf = QLabel(self.topWidgetPdf)
        self.descLabelDestPdf.setObjectName(u"descLabelDestPdf")

        self.verticalLayout_5.addWidget(self.descLabelDestPdf)

        self.destPdf = QWidget(self.topWidgetPdf)
        self.destPdf.setObjectName(u"destPdf")
        self.horizontalLayout_6 = QHBoxLayout(self.destPdf)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnDestPdf = QPushButton(self.destPdf)
        self.btnDestPdf.setObjectName(u"btnDestPdf")

        self.horizontalLayout_6.addWidget(self.btnDestPdf)

        self.labelDestPdf = QLabel(self.destPdf)
        self.labelDestPdf.setObjectName(u"labelDestPdf")

        self.horizontalLayout_6.addWidget(self.labelDestPdf)


        self.verticalLayout_5.addWidget(self.destPdf)


        self.verticalLayout_6.addWidget(self.topWidgetPdf)

        self.verticalSpacer_2 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.bottomWidgetPdf = QWidget(self.pdf)
        self.bottomWidgetPdf.setObjectName(u"bottomWidgetPdf")
        self.horizontalLayout_4 = QHBoxLayout(self.bottomWidgetPdf)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btnCalcPdf = QPushButton(self.bottomWidgetPdf)
        self.btnCalcPdf.setObjectName(u"btnCalcPdf")

        self.horizontalLayout_4.addWidget(self.btnCalcPdf)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addWidget(self.bottomWidgetPdf)

        self.pBarPdf = QProgressBar(self.pdf)
        self.pBarPdf.setObjectName(u"pBarPdf")
        self.pBarPdf.setValue(0)
        self.pBarPdf.setTextVisible(False)

        self.verticalLayout_6.addWidget(self.pBarPdf)

        self.stackedWidget.addWidget(self.pdf)
        self.pdfTuto = QWidget()
        self.pdfTuto.setObjectName(u"pdfTuto")
        self.verticalLayout_8 = QVBoxLayout(self.pdfTuto)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.etapeZeroPdf = QLabel(self.pdfTuto)
        self.etapeZeroPdf.setObjectName(u"etapeZeroPdf")
        self.etapeZeroPdf.setFont(font2)

        self.verticalLayout_8.addWidget(self.etapeZeroPdf)

        self.etapeUnPdf = QLabel(self.pdfTuto)
        self.etapeUnPdf.setObjectName(u"etapeUnPdf")

        self.verticalLayout_8.addWidget(self.etapeUnPdf)

        self.etapeDeuxPdf = QLabel(self.pdfTuto)
        self.etapeDeuxPdf.setObjectName(u"etapeDeuxPdf")
        self.etapeDeuxPdf.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.etapeDeuxPdf)

        self.etapeTroisPdf = QLabel(self.pdfTuto)
        self.etapeTroisPdf.setObjectName(u"etapeTroisPdf")
        self.etapeTroisPdf.setAcceptDrops(False)
        self.etapeTroisPdf.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.etapeTroisPdf)

        self.etapeQuatrePdf = QLabel(self.pdfTuto)
        self.etapeQuatrePdf.setObjectName(u"etapeQuatrePdf")
        self.etapeQuatrePdf.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.etapeQuatrePdf)

        self.stackedWidget.addWidget(self.pdfTuto)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 514, 21))
        self.menuGCODE = QMenu(self.menubar)
        self.menuGCODE.setObjectName(u"menuGCODE")
        self.menuPDF = QMenu(self.menubar)
        self.menuPDF.setObjectName(u"menuPDF")
        self.menuAccueil = QMenu(self.menubar)
        self.menuAccueil.setObjectName(u"menuAccueil")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGCODE.menuAction())
        self.menubar.addAction(self.menuPDF.menuAction())
        self.menubar.addAction(self.menuAccueil.menuAction())
        self.menuGCODE.addAction(self.actionCalculer)
        self.menuGCODE.addAction(self.actionTutorielGcode)
        self.menuPDF.addAction(self.actionExtraire)
        self.menuPDF.addAction(self.actionTutorielPdf)
        self.menuAccueil.addAction(self.actionAccueil)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCalculer.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.actionTutorielGcode.setText(QCoreApplication.translate("MainWindow", u"Tutoriel", None))
        self.actionExtraire.setText(QCoreApplication.translate("MainWindow", u"Extraire", None))
        self.actionTutorielPdf.setText(QCoreApplication.translate("MainWindow", u"Tutoriel", None))
        self.actionAccueil.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selectionnez une action dans la barre en haut a gauche", None))
        self.titleGCODE.setText(QCoreApplication.translate("MainWindow", u"Estimateur code G", None))
        self.descLabelSourceGcode.setText(QCoreApplication.translate("MainWindow", u"Choisir un fichier source :", None))
        self.btnSourceGcode.setText(QCoreApplication.translate("MainWindow", u"Ouvrir ...", None))
        self.labelSourceGcode.setText(QCoreApplication.translate("MainWindow", u"Choisir fichier ...", None))
        self.descLabelDestGcode.setText(QCoreApplication.translate("MainWindow", u"Choisir un ficher de destination (.CSV)  :", None))
        self.btnDestGcode.setText(QCoreApplication.translate("MainWindow", u"Engistrer sous ...", None))
        self.labelDestGcode.setText(QCoreApplication.translate("MainWindow", u"Choisir destination ...", None))
        self.btnCalcGcode.setText(QCoreApplication.translate("MainWindow", u"Lancer \u00e9stimation", None))
        self.etapeZeroGcode.setText(QCoreApplication.translate("MainWindow", u"Comment faire une estimation de temps ?", None))
        self.etapeUnGcode.setText(QCoreApplication.translate("MainWindow", u"1 - Aller dans la barre de menu -> GCode -> Calculer.", None))
        self.etapeDeuxGcode.setText(QCoreApplication.translate("MainWindow", u"2 - Selectionnez votre fichier source, contenant tout le code G que vous souhaitez estimer.", None))
        self.etapeTroisGcode.setText(QCoreApplication.translate("MainWindow", u"3 - Selectionner le fichier de destination CSV. c'est ce fichier Excel dans lequel seront enregistr\u00e9e les estimation ", None))
        self.etapeQuatreGcode.setText(QCoreApplication.translate("MainWindow", u"4 - Lancez l'\u00e9stimation. Vous pouvez ensuite retrouver le fichier Excel au format CSV l\u00e0 o\u00f9 vous l'avez enregistr\u00e9.", None))
        self.titlePDF.setText(QCoreApplication.translate("MainWindow", u"Extracteur data PDF", None))
        self.descLabelSourcePdf.setText(QCoreApplication.translate("MainWindow", u"Choisir les fichiers source :", None))
        self.btnSourcePdf.setText(QCoreApplication.translate("MainWindow", u"Ouvrir ...", None))
        self.labelSourcePdf.setText(QCoreApplication.translate("MainWindow", u"Choisir fichier ...", None))
        self.descLabelDestPdf.setText(QCoreApplication.translate("MainWindow", u"Choisir un ficher de destination (.CSV) :", None))
        self.btnDestPdf.setText(QCoreApplication.translate("MainWindow", u"Engistrer sous ...", None))
        self.labelDestPdf.setText(QCoreApplication.translate("MainWindow", u"Choisir destination ...", None))
        self.btnCalcPdf.setText(QCoreApplication.translate("MainWindow", u"Lancer extration", None))
        self.etapeZeroPdf.setText(QCoreApplication.translate("MainWindow", u"Comment faire une extraction de data ?", None))
        self.etapeUnPdf.setText(QCoreApplication.translate("MainWindow", u"1 - Aller dans la barre de menu ->PDF -> Extraire.", None))
        self.etapeDeuxPdf.setText(QCoreApplication.translate("MainWindow", u"2 - Selectionnez vos fichiesr pdf, utilisez CTRL + Click ou SHIFT + Click pour en selectionner plusieurs..", None))
        self.etapeTroisPdf.setText(QCoreApplication.translate("MainWindow", u"3 - Selectionner le fichier de destination CSV. c'est ce fichier Excel dans lequel seront enregistr\u00e9e les donn\u00e9es", None))
        self.etapeQuatrePdf.setText(QCoreApplication.translate("MainWindow", u"4 - Lancez l'extraction. Ce processus prend 3 \u00e0 4 secondes par fichier. Vous pouvez ensuite trouver les donn\u00e9es dans le fichier Excel au format CSV l\u00e0 o\u00f9 vous l'avez enregistr\u00e9", None))
        self.menuGCODE.setTitle(QCoreApplication.translate("MainWindow", u"GCODE", None))
        self.menuPDF.setTitle(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.menuAccueil.setTitle(QCoreApplication.translate("MainWindow", u"Accueil", None))
    # retranslateUi

