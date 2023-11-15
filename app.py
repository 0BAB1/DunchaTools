#IMPORTS
#générique
import sys ,os, time
# QT & QTDesignerUI imports
from PyQt6.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QMessageBox, QSplashScreen
)
from PyQt6.uic import loadUi
from PyQt6 import QtGui
from interface import Ui_MainWindow
#importer sub-classe de QT customisées
from threads import PdfExctract
# importer les script
from gcodeEstimator import estimation

#to display taskbar icon

class Window(QMainWindow, Ui_MainWindow):
    """Fenetre principale, herite de l'UI réalisée dans QTDesigner (interface.py)"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.setWindowTitle("Duncha toolbox")
        #page par defaut : home page
        self.stackedWidget.setCurrentWidget(self.home)
        #attributs fichiers
        self.sourceFileGcode, self.sourceFilePdf, self.destination = None, None, None
        
    def connectSignalsSlots(self):
        """connecter toutes les action definies dans QtDesigner a leur fonction respective"""
        #Actions de la barre de manu : changements de pages
        self.actionCalculer.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.gcode))
        self.actionTutorielGcode.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.gcodeTuto))
        self.actionExtraire.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.pdf))
        self.actionTutorielPdf.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.pdfTuto))
        self.actionAccueil.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.home))
        
        #clicks de boutons:
        #GCODE
        #bouton pour ouvrir le ficher source
        self.btnSourceGcode.clicked.connect(self.select_file_gcode)
        #bouton pour selectionner le ficher de destination
        self.btnDestGcode.clicked.connect(self.select_dest)
        #bouton pour lancer l'éstimation
        self.btnCalcGcode.clicked.connect(self.run_estimation)
        #PDF
        #bouton pour ouvrir les fichiers sources
        self.btnSourcePdf.clicked.connect(self.select_files_pdf)
        #bouton pour slectionner le fichier de destination
        self.btnDestPdf.clicked.connect(self.select_dest)
        #bouton pour lancer le calcul
        self.btnCalcPdf.clicked.connect(self.run_extraction)
    
    def select_file_gcode(self):
        """selecetionner 1 unique fchier source"""
        file_dialog = QFileDialog()
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                self.labelSourceGcode.setText(selected_file)
                self.sourceFileGcode = selected_file
                
    def select_files_pdf(self):
        """selecetionner plusieurs fchiers source format PDF"""
        file_dialog = QFileDialog(self, "Ouvrir", "", "PDF (*.pdf)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.labelSourcePdf.setText(str(len(selected_files)) + " fichier.s PDF selectionné.s")
                self.sourceFilePdf = selected_files
    
    def select_dest(self):
        """selectionner un fichier de destination forme CSV (format commun pour data output)"""
        fileName, _ = QFileDialog.getSaveFileName(self, "Sauvegarder", "", "CSV(*.csv)")
        if fileName:
            self.destination = fileName
            #j'utilise l amême fonction pour le pdf et le gcode, pas ouf mais bon... on s'est compris haha
            self.labelDestGcode.setText(fileName)
            self.labelDestPdf.setText(fileName)
            
    def run_estimation(self):
        """lancer l'estimation gcode"""
        excel_mode = False
        if self.excelModeBox.isChecked() : excel_mode = True
        
        if not self.sourceFileGcode or not self.destination :
            msg = QMessageBox()
            msg.setText("Erreur interne. Veuillez recommencer.")
            msg.setWindowTitle("Erreur critique !")
            msg.exec()
            return
        
        try :
            open(self.destination, "w+")
            
            data = estimation.run(self.sourceFileGcode, excel_mode=excel_mode)
            estimation.makeCsv(self.destination, data)
    
            msg = QMessageBox()
            msg.setText("Estimation terminée !")
            msg.setWindowTitle("travail terminé !")
            msg.exec()
            return
            
        except Exception as e:
            msg = QMessageBox()
            msg.setText("Error : " + str(e) + " (Permisson error : fermer le finchier CSV et recommencez)")
            msg.setWindowTitle("Erreur critique !")
            msg.exec()
            return

    def run_extraction(self):
        """lancer le thread de l'extraction pdf"""
        if not self.sourceFilePdf or not self.destination :
            msg = QMessageBox()
            msg.setText("Erreur interne. Veuillez recommencer.")
            msg.setWindowTitle("Erreur critique !")
            msg.exec()
            return
        
        
        text_mode = False
        if self.textModeBox.isChecked() : text_mode = True
        #lancer le THREAD PDF
        try :
            open(self.destination, "w+")
            
        except Exception as e:
            msg = QMessageBox()
            msg.setText("Error : " + str(e) + " (Permisson error : fermer le finchier CSV et recommencez)")
            msg.setWindowTitle("Erreur critique !")
            msg.exec()
            
        else:
            self.thread = PdfExctract(self.sourceFilePdf, self.destination, text_mode=text_mode)
            self.thread._signal.connect(self.signal_accept)
            self.thread.start()
            self.btnCalcPdf.setEnabled(False)
    
    def signal_accept(self, msg):
        """traiter les signaux du thread d'extraction PDF"""
        if msg > 0:
            self.pBarPdf.setValue(int(int(msg) * 100 / len(self.sourceFilePdf)))
            
            if self.pBarPdf.value() >= 99:
                #quand la barre de chargement arrive a la fin ...
                self.pBarPdf.setValue(0)
                self.btnCalcPdf.setEnabled(True)
            
                if self.thread.error_occured["value"]:
                    #si erreur durant le traitement, on affiche le message d'erreur
                    msg = QMessageBox()
                    msg.setText("Travail terminé MAIS avec erreur !" + "\n" + self.thread.error_occured["payload"])
                    msg.setWindowTitle("Traitement terminé (avec erreur mineure)")
                    msg.exec()
                else :
                    msg = QMessageBox()
                    msg.setText("travail terminé !")
                    msg.setWindowTitle("Traitement terminé !")
                    msg.exec()
            
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    #loading splash screen
    pixmap = QtGui.QPixmap("./UI/logo/duncha.jpeg")
    splash = QSplashScreen(pixmap=pixmap)
    splash.show()
    splash.showMessage("CHARGEMENT...")
    
    win = Window()
    
    splash.showMessage("Chargement terminé, lancement...")
    
    basedir = os.path.dirname(__file__)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir,"UI", 'logo', 'favicon.ico')))
    win.show()
    splash.hide()
    
    sys.exit(app.exec())