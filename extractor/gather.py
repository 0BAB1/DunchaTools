import os
import pdfplumber as pb
try :
    from . import clear_sorted_data as clear
    from . import sort
except ImportError:
    import clear_sorted_data as clear
    import sort

def getData(file_path : list, text_mode = False) -> list:
    """extraire la data des tableaux d'un fichier pdf"""
    #modele de data : [[ligne 1 du csv final], [ligne2], [etc...], etc...]
    data = []
    
    with pb.open(file_path) as pdf:
        #lire chaque page
        for page in pdf.pages:
            
            try : #sometimes, files are courrupted, so we try and raise an exception taht can be handled in the extraction thread.
                if not text_mode:
                    #extraire les tebleaux de la page
                    tables = page.find_tables()

                    for table in tables:
                        table = table.extract()
                        #lire chaque ligne (de chaque page) (de chque tableau)
                        for line in table:
                            data.append(line)
                        
                elif text_mode:
                    #extraire le texte de la page
                    text = page.extract_text()
                    #lire chaque ligne (de chaque page)
                    for line in text.split("\n"):
                        line = sort.treat_line(line)
                        data.append(line)
                        
            except Exception as e:
                #we raise an error if file is corrupted, file_path.split("/")[0] is the nae of the file at the end of the path
                raise Exception("Erreur FICHIER CORROMPU : " + file_path.split("/")[-1] + "\n" + "Code erreur : " + str(e))
                    
        print(file_path.split("/")[-1] + " was successfully processed ! Processing next file ...")

    return data