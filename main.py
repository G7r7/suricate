import requests
import pandas as pd
import csv
import os
from pydantic import BaseModel
import json

print(pd. __version__)

# nomFichier = 'crimes.xlsx'
# if not os.path.isfile(nomFichier):
#     r = requests.get('https://www.data.gouv.fr/fr/datasets/r/d792092f-b1f7-4180-a367-d043200c1520', allow_redirects=True)
#     if r.status_code == 200:
#         open(nomFichier, 'wb').write(r.content)
# sheet_to_df_map = pd.read_excel(nomFichier, sheet_name="Services GN 2017")
# print(sheet_to_df_map)
# ap = pd.read_excel(nomFichier, sheet_name="Services PN 2017")
# print(sheet_to_df_map)


# nomFichier = 'elections.xlsx'
# if not os.path.isfile(nomFichier):
#     r = requests.get('https://www.data.gouv.fr/fr/datasets/r/53e2b3df-b89b-4df8-971d-7f2e0f02640a', allow_redirects=True)
#     if r.status_code == 200:
#         open(nomFichier, 'wb').write(r.content)
# sheet_to_df_map = pd.read_excel(nomFichier, sheet_name=None)
# print(sheet_to_df_map)


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
#         print(', '.join(row))

# https://stackoverflow.com/questions/69617813/generate-a-json-schema-specification-from-python-classes
# https://github.com/pydantic/pydantic
# https://docs.pydantic.dev/usage/validators/

class Data(BaseModel):
    departement: int
    taux_criminalite: float
    gagnant: str

print(Data.schema_json(indent=2))

external_data = {'departement': 123, 'taux_criminalite': 0.34, 'gagnant': "LePPEN"}
user = Data(**external_data)
print(user)