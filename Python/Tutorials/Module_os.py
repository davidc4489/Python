# Le module os est un module fournit par Python dont le but d'interagir avec le système d'exploitation,
# il permet ainsi de gérer l’arborescence des fichiers, 
# de fournir des informations sur le système d'exploitation processus, variables systèmes, 
# ainsi que de nombreuses fonctionnalités du systèmes...
import os

# os.getlogin() : renvoie le nom d'utilisateur courant.
import os 
user = os.getlogin() 
print(user) # imprime le nom d'utilisateur

# os.mkdir(chemin) : crée un répertoire correspondant au chemin spécifié.
## os.mkdir("/home/mefathim/Documents/My_Folder") # crée un dossier nommé myFolder sur le disque C:\

# os.getcwd() : renvoie le répertoire actuel sous forme de chaîne de caractères.
rep_actuel = os.getcwd()
print(rep_actuel) # renvoie le répertoire actuel

# Afin de pouvoir utiliser la méthode os.path, il faut préalablement importer le module pathlib. 
# Le module pathlib est un module doté d'une interface orientée objet inclus dans python
# depuis la version 3.4 doté de méthodes très intuitives permettant d'interagir 
# avec le système de fichiers d'une façon simple et conviviale.

# La méthode os.path.exist() permet de tester si un répertoire existe ou non
from pathlib import Path
print(os.path.exists("/home/mefathim/Documents"))
#affiche True
# On peut aussi utiliser
print(not os.path.exists("/home/mefathim/Documents"))
#affiche False

# Pour tester la nature d'un chemin s'il s'agit d'un répertoire ou un fichier 
# on utilise les méthodes is_dir() et is_file():
myDirectory = "/home/mefathim/Documents"
p = Path(myDirectory) 
print(p.is_dir()) # affiche True
print(p.is_file()) # affiche False