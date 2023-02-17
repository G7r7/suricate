import re
import requests
import pandas as pd
import csv
import os
from pydantic import BaseModel
import json
from typing import List, Optional

print(pd. __version__)

nomFichier = 'crimes.xlsx'
if not os.path.isfile(nomFichier):
    r = requests.get('https://www.data.gouv.fr/fr/datasets/r/d792092f-b1f7-4180-a367-d043200c1520', allow_redirects=True)
    if r.status_code == 200:
        open(nomFichier, 'wb').write(r.content)
sheet_to_df_map = pd.read_excel(nomFichier, sheet_name="Services GN 2017")
sheet_to_df_map.drop(index=2) # On enlève la ligne des noms de brigades
# On isole les 2 premières colonnes
crimes_index = sheet_to_df_map.iloc[:,0:2]
# We rename the columns with the value of the first row
crimes_index.columns = crimes_index.iloc[0]
crimes_index = crimes_index.iloc[1:]
# On enlève les deux premières colonnes
sheet_to_df_map = sheet_to_df_map.iloc[:,2:]
sheet_to_df_map = sheet_to_df_map.rename(columns=lambda x: re.sub('\.\d+$', '', x))
# Group columns by name and sum values, we ignore null or empty values
sheet_to_df_map = sheet_to_df_map.groupby(sheet_to_df_map.columns, axis=1).sum()

# Class Crime wich is an object with a name, a code and an integer value (with type hints) 
class Crime:
    def __init__(self, name: str, code: str, value: int):
        self.name = name
        self.code = code
        self.value = value

# Class Departement wich containes the name of the departement and an array of object of type Crime with type hints
class Departement:
    def __init__(self, name: str, crimes: List[Crime]):
        self.name = name
        self.crimes = crimes
    
    # Method to calculate the total number of crimes in a departement
    def total_crimes(self) -> int:
        total = 0
        for crime in self.crimes:
            total += crime.value
        return total

# Class Departements which inehrits from List of object of type Departement with type hints
class Departements(List[Departement]):
    pass

# We create an object of type Departements
departements = Departements([])

# Iterate over every column
for col in sheet_to_df_map.columns:
    # For each column we create an Object of type Departement
    # We get the name of the departement from the name of the column
    departement = Departement(str(col), [])
    # We add the crimes to the departement
    for i in range(1, len(sheet_to_df_map[col])):
        # We create an object of type Crime for each entry in the column
        # We get the index code of the crime from crime_index, the index code is the value in column 0
        code = crimes_index.iloc[i-1][0]
        # We get the name of the crime from crime index, the name of the crime is the value on the second column of the row
        name = crimes_index.iloc[i-1][1]
        crime = Crime(name, code, sheet_to_df_map[col].iloc[i])
        # We add the object to the array of crimes
        departement.crimes.append(crime)
    # We add the object to the array of departements
    departements.append(departement)  

# nomFichier = 'elections.xlsx'
# if not os.path.isfile(nomFichier):
#     r = requests.get('https://www.data.gouv.fr/fr/datasets/r/53e2b3df-b89b-4df8-971d-7f2e0f02640a', allow_redirects=True)
#     if r.status_code == 200:
#         open(nomFichier, 'wb').write(r.content)
# sheet_to_df_map = pd.read_excel(nomFichier, sheet_name=None)["Presidentielle_2017_Resultats_Département_T1_clean"]
# interets = sheet_to_df_map[["CodeDépartement", "Département", "LE PEN_exp","MACRON_exp","MÉLENCHON_exp","FILLON_exp","HAMON_exp","DUPONT-AIGNAN_exp","LASSALLE_exp","POUTOU_exp","ASSELINEAU_exp","ARTHAUD_exp","CHEMINADE_exp"]]
# results = interets.iloc[:,-11:]
# # print(results)
# maxResults = results.idxmax(1)
# for i in range(len(maxResults)):
#     print(interets["CodeDépartement"][i], maxResults[i])

# listCol = 
# for col in listCol:
#     print(sheet_to_df_map[col].max())


# nomFichier = 'Departements.csv'
# # if not os.path.isfile(nomFichier):
# #     r = requests.get('https://www.insee.fr/fr/statistiques/fichier/4265429/ensemble.xls', allow_redirects=True)
# #     if r.status_code == 200:
# #         open(nomFichier, 'wb').write(r.content)
# # sheet_to_df_map = pd.read_excel(nomFichier, sheet_name="Départements")
# # print(sheet_to_df_map)
# with open(nomFichier, newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         if len(row) and row[0]:
#             words = ' '.join(row).split(';')
#             dep = words[0]
#             hab = words[-2]
#             print(dep, hab)
#         # print(row[-1].split(';')[-2])

# https://stackoverflow.com/questions/69617813/generate-a-json-schema-specification-from-python-classes
# https://github.com/pydantic/pydantic
# https://docs.pydantic.dev/usage/validators/

class DataForOneDep(BaseModel):
    departement: int
    taux_criminalite: float
    gagnant: str

class Data(BaseModel):
    deps: List[DataForOneDep] = []

# print(Data.schema_json(indent=2))

external_data = {'deps':[{'departement': 123, 'taux_criminalite': 0.34, 'gagnant': "LePPEN"}]}
user = Data(**external_data)
# print(user)
