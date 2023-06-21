# List_Name

# Classement des prénoms masculins et féminins

Ce script Python permet de classer les prénoms masculins et féminins dans un fichier Excel en utilisant des fichiers texte de correspondance.

## Instructions d'utilisation

1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Installez les dépendances requises en exécutant la commande suivante :


3. Placez les fichiers texte "Homme.txt" et "Femme.txt" contenant les correspondances des prénoms masculins et féminins respectivement dans le même répertoire que le script Python.
4. Assurez-vous que le fichier Excel à traiter contient une colonne "Nom" avec les prénoms à classer.
5. Modifiez le nom du fichier Excel dans le script Python, le cas échéant.
6. Exécutez le script Python en utilisant la commande suivante :


7. Le script lira le fichier Excel, classera les prénoms masculins et féminins en utilisant les fichiers texte de correspondance, ajoutera une colonne "Civilité" avec les valeurs correspondantes, puis sauvegardera les modifications dans le fichier Excel initial.

## Remarques

- Assurez-vous d'avoir les fichiers texte "Homme.txt" et "Femme.txt" correctement formatés, un prénom par ligne.
- Le script utilise la bibliothèque pandas pour manipuler les données tabulaires.
- Les résultats du classement seront ajoutés dans une nouvelle colonne "Civilité" du fichier Excel.
- Si un prénom ne correspond à aucun genre défini dans les fichiers texte, la colonne "Civilité" pour cette ligne restera vide.

N'hésitez pas à adapter ce fichier README en fonction de vos besoins spécifiques.
