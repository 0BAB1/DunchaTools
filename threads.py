import sys
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from extractor.gather import getData
        
class PdfExctract(QThread):
    """Thread a lancer pour extraire la data d'une liste de pdf"""
    _signal = pyqtSignal(int)
    def __init__(self, file_list, destination):
        super(PdfExctract, self).__init__()
        self.file_list = file_list
        self.destination = destination
        
    def __del__(self):
        self.wait()
        
    def run(self):
        data = []
        i = 0
        for file in self.file_list:
            i += 1
            dataTemp = []
            dataTemp = getData(file)
            for item in dataTemp:
                data.append(item)
            self._signal.emit(i)
        with open(self.destination, "w+") as dest :
            for line in data:
                for element in line :
                    dest.write(str(element).replace("\n","") + ";")
                dest.write("\n")
        