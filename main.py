import re
import requests
import pandas as pd
import csv
import os
from pydantic import BaseModel
import json
from typing import List, Optional

# Class Crime wich is an object with a name, a code and an integer value (with type hints) 
class Crime:
    def __init__(self, name: str, code: str, value: int):
        self.name = name
        self.code = code
        self.value = value

# Class Departement wich containes the name of the departement and an array of object of type Crime with type hints
class Departement:
    def __init__(self, code: str, name: str, gagnant: str, population: int, crimes: List[Crime]):
        self.code = code
        self.name = name
        self.crimes = crimes
        self.gagnant = gagnant
        self.population = population
    
    # Method to calculate the total number of crimes in a departement
    def total_crimes(self, codes: List[int]) -> int:
        total = 0
        for crime in self.crimes:
            if crime.code in codes or len(codes) == 0: # if the code of the crime is in the list of codes or if the list of codes is empty
                total += crime.value
        return total

    def taux_crime(self, codes: List[int]) -> float:
        return round(self.total_crimes(codes) / self.population * 100, 8)

# Class Departements which inehrits from List of object of type Departement with type hints
class Departements(List[Departement]):
    pass

print(pd. __version__)

nomFichier = 'elections.xlsx'
# if not os.path.isfile(nomFichier):
#     r = requests.get('https://www.data.gouv.fr/fr/datasets/r/53e2b3df-b89b-4df8-971d-7f2e0f02640a', allow_redirects=True)
#     if r.status_code == 200:
#         open(nomFichier, 'wb').write(r.content)
sheet_to_df_map = pd.read_excel(nomFichier, sheet_name=None)["Presidentielle_2017_Resultats_Département_T1_clean"]
interets = sheet_to_df_map[["CodeDépartement", "Département", "LE PEN_exp","MACRON_exp","MÉLENCHON_exp","FILLON_exp","HAMON_exp","DUPONT-AIGNAN_exp","LASSALLE_exp","POUTOU_exp","ASSELINEAU_exp","ARTHAUD_exp","CHEMINADE_exp"]]
results = interets.iloc[:,-11:]
# print(results)
maxResults = results.idxmax(1)

# We create a list of departements
departements = Departements()

for i in range(len(maxResults)):
    dep = str(interets["CodeDépartement"][i])
    res = maxResults[i][:-4]
    if dep[0] != 'Z': #on retire les outres mers
        if len(dep) == 1:
            dep = '0'+dep
            # print(dep, interets["Département"][i], res)
        # We add a departement to the list where the departement code is dep, the departement name is interets["Département"][i], the gagnant is res and the list of crimes is empty and population is 0
        departements.append(Departement(dep, interets["Département"][i], res, 0, []))

nomFichier = 'Departements.csv'
# if not os.path.isfile(nomFichier):
#     r = requests.get('https://www.insee.fr/fr/statistiques/fichier/4265429/ensemble.xls', allow_redirects=True)
#     if r.status_code == 200:
#         open(nomFichier, 'wb').write(r.content)
# sheet_to_df_map = pd.read_excel(nomFichier, sheet_name="Départements")
# print(sheet_to_df_map)
with open(nomFichier, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) and row[0]:
            words = ' '.join(row).split(';')
            dep = words[0]
            hab = words[-2]
            if len(dep) == 2: #on retire les outres mers
                # print(dep, hab)
                # We add the population to the departement with the code dep
                for departement in departements:
                    if departement.code == dep:
                        departement.population = int(hab)


nomFichier = 'crimes.xlsx'
if not os.path.isfile(nomFichier):
    r = requests.get('https://www.data.gouv.fr/fr/datasets/r/d792092f-b1f7-4180-a367-d043200c1520', allow_redirects=True)
    if r.status_code == 200:
        open(nomFichier, 'wb').write(r.content)

# Crime index
sheet = pd.read_excel(nomFichier, sheet_name="Services GN 2017")
# On isole les 2 premières colonnes
crimes_index = sheet.iloc[:,0:2]
# We rename the columns with the value of the first row
crimes_index.columns = crimes_index.iloc[0]
# On enlève la ligne contenant le nom des colonnes
crimes_index.drop(index=0, inplace=True) 

# Gendarmerie
gendarmerie = pd.read_excel(nomFichier, sheet_name="Services GN 2017")
# On enlève la ligne des noms de brigades
gendarmerie.drop(index=0, inplace=True) 
# On enlève les 2 premières colonnes
gendarmerie = gendarmerie.iloc[:,2:]
# On renomme les colonnes 91.1 91.2 91.3 en 91 ...
gendarmerie = gendarmerie.rename(columns=lambda x: re.sub('\.\d+$', '', x))
# On enlèves les colonnes dont le nom est plus long que 2 caractères
gendarmerie = gendarmerie.loc[:, gendarmerie.columns.str.len() <= 2]
# Group columns by name and sum values, we ignore null or empty values
gendarmerie = gendarmerie.groupby(gendarmerie.columns, axis=1).sum()
# We rename rows with 0,1,2...
gendarmerie.reset_index(inplace=True, drop=True)

# Police
police = pd.read_excel(nomFichier, sheet_name="Services PN 2017")
# On enlève la ligne des noms de brigades
police.drop(index=1, inplace=True)
# On enlève la ligne des noms de brigades
police.drop(index=0, inplace=True)
# On enlève les deux premières colonnes
police = police.iloc[:,2:]
# On renomme les colonnes 91.1 91.2 91.3 en 91 ...
police = police.rename(columns=lambda x: re.sub('\.\d+$', '', x))
# On enlèves les colonnes dont le nom est plus long que 2 caractères
police = police.loc[:, police.columns.str.len() <= 2]
# Group columns by name and sum values, we ignore null or empty values
police = police.groupby(police.columns, axis=1).sum()
# We rename rows with 0,1,2...
police.reset_index(inplace=True, drop=True)

# We add the two dataframes (integers)
crimes = gendarmerie.add(police, fill_value=0)

# For each departement we add the crimes
for departement in departements:
    # We get the column with the code of the departement
    col = crimes[departement.code]
    # We iterate over the column
    for i in range(1, len(col)):
        # We create an object of type Crime for each entry in the column
        # We get the index code of the crime from crime_index, the index code is the value in column 0
        code = crimes_index.iloc[i-1][0]
        # We get the name of the crime from crime index, the name of the crime is the value on the second column of the row
        name = crimes_index.iloc[i-1][1]
        crime = Crime(name, code, col.iloc[i])
        # We add the object to the array of crimes
        departement.crimes.append(crime)


# https://stackoverflow.com/questions/69617813/generate-a-json-schema-specification-from-python-classes
# https://github.com/pydantic/pydantic
# https://docs.pydantic.dev/usage/validators/

class DataForOneDep(BaseModel):
    departement: str
    taux_criminalite: float
    gagnant: str

class Data(BaseModel):
    deps: List[DataForOneDep] = []

# print(Data.schema_json(indent=2))

external_data = {}
external_data['deps'] = []
for departement in departements:
    external_data['deps'].append({'departement': departement.code, 'taux_criminalite': departement.taux_crime([2,3]), 'gagnant': departement.gagnant})

user = Data(**external_data)

# We export json to file
with open('data.js', 'w') as outfile:
    outfile.write('const external_data = ')
    json.dump(user.dict(), outfile, indent=2)
    