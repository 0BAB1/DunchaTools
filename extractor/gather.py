# ====================================================================
# Defines functions to get data from the PDF file out in a table/list 
# ====================================================================

import os
import pdfplumber as pb
# Had some problem while doing imports for tests cases so i used both methods :
try :
    from . import sort
except ImportError:
    import sort

def treat_line(line : str) -> list:
    """Return the imput as a splited list"""
    # I use space for now and it's doing great ! could improve by allowing user to customize separators
    line = line.split(" ")
    return line

def getData(file_path : list, text_mode = False) -> list:
    """extraire la data des tableaux d'un fichier pdf. Set text_mode to True if you want raw data or Flase if you want to extract table structures"""
    # modele de data : [[ligne 1 du csv final], [ligne2], [etc...], etc...]
    data = []
    
    with pb.open(file_path) as pdf:
        #lire chaque page
        for page in pdf.pages:
            
            # Sometimes, files are courrupted which crashes the PyQt app extraction thread (when batch extract using the app)
            # To avoid this bug, we try and raise an Exception that will be aknoleged by the thread and the file will be skipped (and user will be informed)
            try : 
                if not text_mode:
                    #extraire les tebleaux de la page
                    tables = page.find_tables()

                    for table in tables:
                        table = table.extract()
                        #lire chaque ligne (de chaque page) (de chque tableau)
                        for line in table:
                            line.insert(0, sort.get_file_name(file_path)) # add the fileName at each line
                            data.append(line)
                        
                elif text_mode:
                    #extraire le texte de la page
                    text = page.extract_text()
                    #lire chaque ligne
                    for line in text.split("\n"):
                        line = treat_line(line) # reutrns line as raw splited list
                        line.insert(0, sort.get_file_name(file_path)) # add the fileName at each line
                        data.append(line)
                        
            except Exception as e:
                # We raise an error if file is corrupted
                raise Exception("Erreur FICHIER CORROMPU : " + sort.get_file_name(file_path) + "\n" + "Code erreur : " + str(e))
                    
        print(sort.get_file_name(file_path) + " was successfully processed ! Processing next file ...")

    return data