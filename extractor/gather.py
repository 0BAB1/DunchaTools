import os
import pdfplumber as pb
from . import clear_sorted_data as clear
from . import sort

def getData(file_path : list) -> list:
    """extraire la data des tableaux d'un fichier pdf"""
    #modele de data : [[ligne 1 du csv final], [ligne2], [etc...], etc...]
    data = []
    
    with pb.open(file_path) as pdf:
        #lire chaque page
        for page in pdf.pages:
            #extraire les tebleaux de la page
            tables = page.find_tables()

            for table in tables:
                table = table.extract()
                #lire chaque ligne (de chaque page) (de chque tableau)
                for line in table:
                    data.append(line)

        print(file_path.split("/")[-1] + " was successfully processed ! Processing next file ...")

    return data