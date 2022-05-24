# ls_chesstournament
Projet 4 du parcours développeur Python d'OpenClassroom




## Installation de l'environnement virtuel

Afin de garentir le bon fonctionnement de ce programme, vous devez l'exécuter dans le même environnement virtuel que le développeur. Pour se faire, suivez les instructions d'installation ci-dessous.
Attention, nous partons du principe que les paquets pip et venv sont bien installés sur votre ordinateur. Si tel n'est pas le cas, veuillez vous référer à leur documentation respective pour procéder à leur installation.


### Installation sous Windows

1- Ouvrez l'invite de commandes

2- Déplacez-vous à la racine du dossier ls_chesstournament, à l'aide de la commande cd

3- Pour créer l'environnement virtuel, saisissez la commande : `python -m venv env`

4- Pour démarrer ce dernier, saisissez la commande : `env\Scripts\activate`

5- Pour y installer les paquets nécessaires à la bonne exécution du script, saisissez la commande : `pip install -r requirements.txt`


### Installation sous Linux ou MacOSX

1- Ouvrez un terminal

2- Déplacez-vous à la racine du dossier ls_chesstournament, à l'aide de la commande cd

3- Pour créer l'environnement virtuel, saisissez la commande : `python -m venv env`

4- Pour démarrer ce dernier, saisissez la commande : `source env/bin/activate`

5- Pour y installer les paquets nécessaires à la bonne exécution du script, saisissez la commande : `pip install -r requirements.txt`



## Utilisation de Flake8

Afin de vérifier que le code du programme répond bien à la norme PEP-8, vous pouvez utiliser la commande Flake8.

Pour que Flake8 affiche son rapport directement dans la console : 

1- Déplacez-vous à la racine du dossier ls_chesstournament, à l'aide de la commande cd

2- puis saisissez la commande `flake8 src`

Pour générer un rapport au format html :

1- Déplacez-vous à la racine du dossier ls_chesstournament, à l'aide de la commande cd

2- puis saisissez la commande `flake8 --format=html --htmldir=flake8_rapport src`

3- Déplacez vous dans le dossier "flake8_rapport", puis ouvrez le fichier "index.html", pour y trouver le rapport de Flake8.



## Lancement du programme

Attention, avant de lancer le programme, assurez-vous que l'environnement virtuel est activé.

1- Ouvrez l'invite de commandes

2- Déplacez-vous à la racine du dossier ls_chesstournament, à l'aide de la commande cd

3- Si vous êtes sous Windows, saisissez la commande `python src\chesstournament.py`, sous Linux ou MacOSX saisissez la commande `python src/chesstournament.py`



## Utilisation du programme

Le programme a été consu pour que son utilisation soit la plus simple possible :

Pour naviguer, saisissez le chiffre se trouvant devant l'élément de menu que vous souhaitez invoquer, puis appuyez sur "Entrer".

Pour saisir les données d'un formulaire, servez vous des informations d'aide entre parenthèses.

L'état du programme est constemment sauvegardé, ainsi aucun risque de perte de données.

Pour quitter le programme, vous pouvez naviguer jusqu'au menu principal, saisir le chiffre 3, puis appuyer sur la touche "Entrer"; ou utiliser le raccourci clavier "CTRL+C" à tout moment.
