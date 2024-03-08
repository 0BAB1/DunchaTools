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
        # Exception can occur while trying to extract corrupted files
        # to handle that, we simply ignr the corrupted file and goto the next
        # but we keep track of exception raise by the extracto in this dict to properly inform the user of corrupted files
        # If we have exceptions, value turns to True and we add error message to "payload" (just a global message gathring all raised Exception messages)
        self.error_occured = {"value" : False, "payload" : ""}
        
    def __del__(self):
        self.wait()
        
    def run(self):
        data = []
        i = 0
        for file in self.file_list:
            i += 1
            dataTemp = []
            
            # getData raises an error in case of a corrupt file, so we handle it
            try :
                # Extract data using the pdf extractor
                dataTemp = getData(file, text_mode = self.text_mode)
                for item in dataTemp:
                    data.append(item)
                self._signal.emit(i)
                
            except Exception as e:
                # Handle Exception raised by the extractor and goto next PDF file
                self.error_occured["value"] = True
                self.error_occured["payload"] += str(e)
                self.error_occured["payload"] += "\n \n"
                dataTemp = []
                self._signal.emit(i)
                
        with open(self.destination, "w+") as dest :
            # Once finished, write global data in CSV destination file
            for line in data:
                for element in line :
                    dest.write(str(element).replace("\n","").replace(".", ",") + ";")
                dest.write("\n")
        
        