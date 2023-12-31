import sys
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import QMessageBox
from extractor.gather import getData
        
class PdfExctract(QThread):
    """Thread a lancer pour extraire la data d'une liste de pdf"""
    _signal = pyqtSignal(int)
    def __init__(self, file_list, destination, text_mode = False):
        super(PdfExctract, self).__init__()
        self.file_list = file_list
        self.destination = destination
        self.text_mode = text_mode
        
        self.error_occured = {"value" : False, "payload" : ""} #error value and message to read at the end of the thread to notify the user
        
    def __del__(self):
        self.wait()
        
    def run(self):
        data = []
        i = 0
        for file in self.file_list:
            i += 1
            dataTemp = []
            
            #getData raises an error in case of a corrupt file, so we handle it
            try :
                #regular routine
                dataTemp = getData(file, text_mode = self.text_mode)
                for item in dataTemp:
                    data.append(item)
                self._signal.emit(i)
                
            except Exception as e:
                #si erreur, on emment un signal avec e
                self.error_occured["value"] = True
                self.error_occured["payload"] += str(e)
                self.error_occured["payload"] += "\n \n"
                dataTemp = []
                self._signal.emit(i)
                
        with open(self.destination, "w+") as dest :
            for line in data:
                for element in line :
                    dest.write(str(element).replace("\n","").replace(".", ",") + ";")
                dest.write("\n")
        
        