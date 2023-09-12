#IMPORTS
#générique
import sys
# QT & QTDesignerUI imports
from PyQt6.QtWidgets import (
    QApplication, QFileDialog, QMainWindow,
)
from PyQt6.uic import loadUi
from interface import Ui_MainWindow
#importer sub-classe de QT customisées
from threads import PdfExctract
# importer les script
from calculator import calc

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
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
        if not self.sourceFileGcode or not self.destination : return False
        data = calc.calc(self.sourceFileGcode)
        with open(self.destination, "w+") as file :
            file.write("temps total :" + ";" + str(data[0]) + "\n")
            for line in data[1]:
                for columnElement in line:
                    file.write(str(columnElement).replace(".",",") + ";")
                file.write("\n")
        return True

    def run_extraction(self):
        """lancer le thread de l'extraction pdf"""
        if not self.sourceFilePdf or not self.destination : return False
        #lancer le THREAD PDF
        self.thread = PdfExctract(self.sourceFilePdf, self.destination)
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.btnCalcPdf.setEnabled(False)
    
    def signal_accept(self, msg):
        """traiter les signaux du thread PDF"""
        self.pBarPdf.setValue(int(int(msg) * 100 / len(self.sourceFilePdf)))
        if self.pBarPdf.value() >= 99:
            self.pBarPdf.setValue(0)
            self.btnCalcPdf.setEnabled(True)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())