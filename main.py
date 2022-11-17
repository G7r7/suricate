import requests
import pandas as pd

r = requests.get('https://www.data.gouv.fr/fr/datasets/r/d792092f-b1f7-4180-a367-d043200c1520', allow_redirects=True)
nomFichierCrime = '/workspaces/suricate/crimes-et-delits-enregistres-par-les-services-de-gendarmerie-et-de-police-depuis-2012.xlsx'
if r.status_code == 200:
    open(nomFichierCrime, 'wb').write(r.content)

df = pd.read_excel(nomFichierCrime, engine='openpyxl')
print(df)