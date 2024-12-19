import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Ols import OrdinaryLeastSquares

"""Première partie est traiter les données qui est très sale  
qui est jusqu'à ligne 110"""

# Supposons que les données sont stockées dans un fichier nommé 'data.csv'
data = pd.read_csv(r'Base_Carbone_V23.4.csv', sep=',',
                   quotechar='"', encoding='latin-1', low_memory=False)

# Ouvrir le fichier et vérifier son contenu
file_path = r'Base_Carbone_V23.4.csv'
# Afficher les informations et les noms des colonnes des données (pour débogage)
# print(data.info())
#print(data.columns)

# Chaîne des noms de colonnes d'origine (inclut des guillemets et des caractères
# superflus à nettoyer)
columns_string = ('"Type Ligne";"Identifiant de l\'\u00e9l\u00e9ment";Structure;'
                  '"Type de l\'\u00e9l\u00e9ment";"Statut de l\'\u00e9l\u00e9ment";'
                  '"Nom base fran\u00e7ais";"Nom base anglais";"Nom base espagnol";'
                  '"Nom attribut fran\u00e7ais";"Nom attribut anglais";'
                  '"Nom attribut espagnol";"Nom fronti\u00e8re fran\u00e7ais";'
                  '"Nom fronti\u00e8re anglais";"Nom fronti\u00e8re espagnol";'
                  '"Code de la cat\u00e9gorie";"Tags fran\u00e7ais";"Tags anglais";'
                  '"Tags espagnol";"Unit\u00e9 fran\u00e7ais";"Unit\u00e9 anglais";'
                  '"Unit\u00e9 espagnol";Contributeur;"Autres Contributeurs";'
                  'Programme;"Url du programme";Source;"Localisation g\u00e9ographique";'
                  '"Sous-localisation g\u00e9ographique fran\u00e7ais";'
                  '"Sous-localisation g\u00e9ographique anglais";'
                  '"Sous-localisation g\u00e9ographique espagnol";'
                  '"Date de cr\u00e9ation";"Date de modification";'
                  '"P\u00e9riode de validit\u00e9";Incertitude;R\u00e9glementations;'
                  'Transparence;Qualit\u00e9;"Qualit\u00e9 TeR";"Qualit\u00e9 GR";'
                  '"Qualit\u00e9 TiR";"Qualit\u00e9 C";"Qualit\u00e9 P";"Qualit\u00e9 M";'
                  '"Commentaire fran\u00e7ais";"Commentaire anglais";'
                  '"Commentaire espagnol";"Type poste";"Nom poste fran\u00e7ais";'
                  '"Nom poste anglais";"Nom poste espagnol";'
                  '"Total poste non d\u00e9compos\u00e9";CO2f,CH4f,CH4b,N2O;'
                  '"Code gaz suppl\u00e9mentaire 1";"Valeur gaz suppl\u00e9mentaire 1";'
                  '"Code gaz suppl\u00e9mentaire 2";"Valeur gaz suppl\u00e9mentaire 2";'
                  '"Code gaz suppl\u00e9mentaire 3";"Valeur gaz suppl\u00e9mentaire 3";'
                  '"Code gaz suppl\u00e9mentaire 4";"Valeur gaz suppl\u00e9mentaire 4";'
                  '"Code gaz suppl\u00e9mentaire 5";"Valeur gaz suppl\u00e9mentaire 5";'
                  '"Autres GES";CO2b')

# Diviser les noms de colonnes par des points-virgules
columns_list = columns_string.split(';')

# Nombre cible de colonnes (nombre attendu de noms de colonnes)
desired_columns_count = 75

# Supprimer les guillemets doubles et les espaces inutiles de chaque nom de colonne
columns_list = [col.strip().strip('"') for col in columns_list]

# Nombre actuel de colonnes
current_columns_count = len(columns_list)
# print(f"Nombre de colonnes après division : {current_columns_count}")

# Si le nombre de colonnes est insuffisant, compléter jusqu'au nombre cible
if current_columns_count < desired_columns_count:
    columns_list += [f"Unnamed_{i}" for i in range(current_columns_count, desired_columns_count)]

# Si le nombre de colonnes dépasse, couper jusqu'au nombre cible
columns_list = columns_list[:desired_columns_count]

# Afficher la liste finale des noms de colonnes
# print(f"Nombre de colonnes après ajustement : {len(columns_list)}")
# print(columns_list)

# Lire et traiter les grandes fichiers ligne par ligne, en sautant la ligne des noms de colonnes d'origine


# Diviser chaque ligne de données en une liste basée sur des points-virgules
df=[]
with open(r'Base_Carbone_V23.4.csv', 'r', encoding='latin-1') as file:
    for line in file:
        values = line.strip().split(';')  # Supprimer les caractères de fin de ligne et diviser par des virgules
        values = [col.strip().strip('"') for col in values]
        #print(values)
        df.append(values)
df = df[1:]

data = pd.DataFrame(df, columns=columns_list)

# Mapper les données divisées dans un DataFrame
#data = pd.DataFrame(data_split)
#data.columns = ['col1', 'col2', 'col3','col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10','col11', 'col12', 'col13', 'col14', 'col15', 'col16', 'col17', 'col18', 'col19','col20']
# Enregistrer les données traitées dans un fichier Excel
output_file = 'processed_data.xlsx'
data['Total poste non décomposé'] = (
    data['Total poste non décomposé'].fillna('').str.replace(',', '.'))
data['Total poste non décomposé'] = (
    data['Total poste non décomposé'].str.replace('"', '', regex=False))
#data.to_excel(output_file, index=False)
# index=False pour ne pas enregistrer les index des lignes


non_empty_co2b = data[data['CO2b'].notnull()]

outp1ut_file = 'processed_data.xlsx'

# Conserver les colonnes spécifiques
columns_to_keep = ['Nom base français', 'Tags français', 'Unité français',
                   'Total poste non décomposé',
                   'Commentaire français','Qualité','Nom attribut français']
data=data[columns_to_keep]
data = pd.DataFrame(data)

#Convertir les nombres avec un E en int ou float
data['Total poste non décomposé']= pd.to_numeric(data['Total poste non décomposé'],
                                                 errors='coerce')


""""Second Partie est résumer les CO2 en moyenne du chaque type dans une CVS
Et je faire pour les aliment et pour l'égernie comme le méthod je deja connaitre 
je utilise le fihsher vous proposé"""

category_mapping = {
    "Viande": ["boeuf", "agneau", "porc", "poulet", "canard", "poisson", "viande"],
    "Céréales": ["riz", "farine", "blé", "maïs","Céréales","Barre céréalière"],
    "Légumes": ["légumes", "épinards", "tomates", "pommes de terre", "concombre"],
    "Produits laitiers": ["lait", "beurre", "fromage", "produit laitier"],
    "Produits à base de soja": ["tofu", "lait de soja", "soja"],
    "Fruits": ["pomme", "banane", "orange", "fraise", "raisin",
               "citron", "pastèque", "fruits","abricot"],
    "Alcool": ["Bière","Apéritifs","Vin","Spirits"],
    "Boissons": [
        "red bull", "monster", "burn", "boisson énergisante",
        "eau gazeuse", "eau plate", "limonade", "soda", "jus de fruits",
        "nectar", "smoothie","café", "espresso", "cappuccino", "latte",
        "thé", "tisane", "chocolat chaud"
    ],
    "Avion":["avion"],
    "Bus":["Bus"],
    "Voiture":["Voiture"],
}
#print("Unite",data["Unité français"].unique())
def classify_food(food_name):
    # S'assurer que food_name est converti en minuscules
    food_name_lower = food_name.lower()
    for category, keywords in category_mapping.items():
        # Parcourir les mots-clés en ignorant la casse
        if any(keyword.lower() in food_name_lower for keyword in keywords):
            return category
    return "autre"  # Si aucune correspondance n'est trouvée, classer comme "autre"


# 3. Appliquer la fonction de classification
data["categori"] = data["Nom base français"].apply(classify_food)
filtered_data = data[
    ~(
        ((data["categori"] == "Légumes") & (data["Total poste non décomposé"] > 20)) |
        ((data["categori"] == "Céréales") & (data["Total poste non décomposé"] > 20)) |
        ((data["categori"] == "Fruits") & (data["Total poste non décomposé"] > 20)) |
        ((data["categori"] == "Alcool") & (data["Total poste non décomposé"] > 60)) |
        ((data["categori"] == "Boissons") & (data["Total poste non décomposé"] > 30)) |
        ((data["categori"] == "Bus") & (data["Total poste non décomposé"] > 1)) |
        (data["categori"] == "autre")
    )
]
# Enregistrer le résultat dans un fichier CSV
(filtered_data[["categori", "Total poste non décomposé"]]
 .to_csv("filtered_output.csv", index=False, encoding="utf-8"))

means = filtered_data[filtered_data["Total poste non décomposé"] > 0].groupby("categori")["Total poste non décomposé"].mean()
"""
bus_rows = data[data["categori"]== "Bus"]
bus_rows.to_csv("BUS.csv", index=True, header=True, encoding='latin-1')
"""

means.to_csv("means_output.csv", index=True, header=True, encoding='latin-1')
print("FILE")
