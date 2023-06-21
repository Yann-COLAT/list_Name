import pandas as pd

# Chargement du fichier Excel
df = pd.read_excel("C:\\Users\\yann.colat\\Lost-Name\\PRENOM\\test_gender_api.xlsx")

# Chargement des correspondances homme/femme depuis les fichiers texte
with open("C:\\Users\\yann.colat\\Lost-Name\\PRENOM\\Homme.txt", "r") as f:
    hommes = set(f.read().splitlines())

with open("C:\\Users\\yann.colat\\Lost-Name\\PRENOM\\Femme.txt", "r") as f:
    femmes = set(f.read().splitlines())

# Création de la colonne "Civilité"
df["Civilité"] = ""

# Parcours de chaque ligne du DataFrame
for index, row in df.iterrows():
    prenom = row["Nom"]
    
    # Classement du prénom en fonction du genre
    if prenom in hommes:
        civ = "M."
    elif prenom in femmes:
        civ = "Mme"
    else:
        civ = ""  # Si le prénom n'est pas trouvé dans les fichiers texte, laisser la civilité vide
    
    # Assignation de la civilité dans la colonne correspondante
    df.at[index, "Civilité"] = civ

# Sauvegarde du DataFrame modifié dans le fichier Excel
df.to_excel("C:\\Users\\yann.colat\\Lost-Name\\PRENOM\\test_gender_api.xlsx", index=False)
