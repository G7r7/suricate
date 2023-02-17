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
print(sheet_to_df_map)


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

print(Data.schema_json(indent=2))

external_data = {'deps':[{'departement': 123, 'taux_criminalite': 0.34, 'gagnant': "LePPEN"}]}
user = Data(**external_data)
print(user)
