# Suricate

![](images/suricate.jpg)

## About

Suricate is a dataset aggregator and website to browse. 
It ingests and connects data relative to political elections, socio-professional categories and crimes and infractions in France.

## Prerequisites

```shell
pip install requests
pip install pandas
pip install pydantic
pip install odfpy
pip install openpyxl
```

## Exemple

Will generate the corresponding the `data.js` file for `vol à la roulotte` (37) and `Chasse et pêche` (80):
```
python main.py 37 80
```

Then we open the `index.html` in any browser and get:

![](images/map.png)

## Usage

```
usage: python main.py [<crime index>...]
parameters:
crime-index: crime index that we will be added to the calculation (default: all indexes) 
List of available crime indexes:
1 Règlements de compte entre malfaireurs
2 Homicides pour voler et à l'occasion de vols
3 Homicides pour d'autres motifs
4 Tentatives d'homicides pour voler et à l'occasion de vols
5 Tentatives homicides pour d'autres motifs
6 Coups et blessures volontaires suivis de mort
7 Autres coups et blessures volontaires criminels ou correctionnels
8 Prises d'otages à l'occasion de vols
9 Prises d'otages dans un autre but
10 Sequestrations
11 Menaces ou chantages pour extorsion de fonds
12 Menaces ou chantages dans un autre but
13 Atteintes à la dignité et à la  personnalité
14 Violations de domicile
15 Vols à main armée contre des établissements financiers
16 Vols à main armée contre des éts industriels ou commerciaux
17 Vols à main armée contre des entreprises de transports de fonds
18 Vols à main armée contre des particuliers à leur domicile
19 Autres vols à main armée
20 Vols avec armes blanches contre des établissements financiers,commerciaux ou industriels
21 Vols avec armes blanches contre des particuliers à leur domicile
22 Autres vols avec armes blanches
23 Vols violents sans arme contre des établissements financiers,commerciaux ou industriels
24 Vols violents sans arme contre des particuliers à leur domicile
25 Vols violents sans arme contre des femmes sur voie publique ou autre lieu public
26 Vols violents sans arme contre d'autres victimes
27 Cambriolages de locaux d'habitations principales
28 Cambriolages de résidences secondaires
29 Camb.de  locaux industriels, commerciaux ou financiers
30 Cambriolages d'autres lieux
31 Vols avec entrée par ruse en tous lieux
32 Vols à la tire
33 Vols à l'étalage
34 Vols de véhicules de transport avec frêt
35 Vols d'automobiles
36 Vols de véhicules motorisés à 2 roues
37 Vols à la roulotte
38 Vols d''accessoires sur véhicules à moteur immatriculés
39 Vols simples sur chantier
40 Vols simples sur exploitations agricoles
41 Autres vols simples contre des établissements publics ou privés
42 Autres vols simples contre des particuliers dans  deslocaux privés
43 Autres vols simples contre des particuliers dans des locaux ou lieux publics
44 Recels
45 Proxénétisme
46 Viols sur des majeur(e)s
47 Viols sur des mineur(e)s
48 Harcèlements sexuels et autres agressions sexuelles contre des majeur(e)s
49 Harcèlements sexuels et autres agressions sexuelles contre des mineur(e)s
50 Atteintes sexuelles
51 Homicides commis contre enfants de moins de 15 ans
52 Violences, mauvais traitements et abandons d'enfants.
53 Délits au sujet de la garde des mineurs
54 Non versement de pension alimentaire
55 Trafic et revente sans usage de stupéfiants
56 Usage-revente de stupéfiants
57 Usage de stupéfiants
58 Autres infractions à la législation sur les stupéfiants
59 Délits de débits de boissons et infraction à la règlementation sur l'alcool  et le tabac
60 Fraudes alimentaires et infractions à l'hygiène
61 Autres délits contre santé publique et la réglementation des professions médicales
62 Incendies volontaires de biens publics
63 Incendies volontaires de biens privés
64 Attentats à l'explosif contre des biens publics
65 Attentats à l'explosif contre des biens privés
66 Autres destructions er dégradations de biens publics
67 Autres destructions er dégradations de biens privés
68 Destructions et dégradations de véhicules privés
69 Infractions aux conditions générales d'entrée et de séjour des étrangers
70 Aide à l'entrée, à la circulation et au séjour des étrangers
71 Autres infractions à la police des étrangers
72 Outrages à dépositaires autorité
73 Violences à dépositaires autorité
74 Port ou détention armes prohibées
75 Atteintes aux intérêts fondamentaux de la Nation
76 Délits des courses et des jeux
77 Délits interdiction de séjour et de paraître
78 Destructions, cruautés et autres délits envers les animaux
79 Atteintes à l'environnement
80 Chasse et pêche
81 Faux documents d'identité
82 Faux documents concernant la circulation des véhicules
83 Autres faux documents administratifs
84 Faux en écriture publique et authentique
85 Autres faux en écriture
86 Fausse monnaie
87 Contrefaçons et fraudes industrielles et commerciales
88 Contrefaçons littéraires et artistique
89 Falsification et usages de chèques volés
90 Falsification et usages de cartes de crédit
91 Escroqueries et abus de confiance
92 Infractions à la législation sur les chèques
93 Travail clandestin
94 Emploi d'étranger sans titre de travail
95 Marchandage - prêt de main d'oeuvre
96 Index non utilisé
97 Index non utilisé
98 Banqueroutes, abus de biens sociaux et autres délits de société
99 Index non utilisé
100 Index non utilisé
101 Prix illicittes, publicité fausse et infractions aux règles de la concurrence
102 Achats et ventes sans factures
103 Infractions à l'exercice d'une profession règlementée
104 Infractions au droit de l'urbanisme et de la construction
105 Fraudes fiscales
106 Autres délits économiques et financiers
107 Autres délits
```
