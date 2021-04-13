import pandas as pd
import math

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_public.csv"
                , index_col = 'Respondent')
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_schema.csv"
                        , index_col = 'Column')

df['ConvertedComp'].head(15)

df['ConvertedComp'].median() # Median =/= Mean (more realistic when there is a big gap between average and highest value)
df.median() # Trouve les colonnes avec des valeurs numérique
df.describe() # Différentes statistiques (count, mean, std, min, etc..) 
df['ConvertedComp'].count() # Nombre de valeur
df['Hobbyist'].value_counts() # Compte selon la réponse,

df['Employment'].value_counts(normalize = True) # ...  avec l'option normalize, donne en %

# Avec les filtres :
filt = df['Country'] == 'India'
df.loc[filt]
df.loc[filt]['Employment'].value_counts() # 

# Avec la méthode groupby

country_grp = df.groupby(['Country']) # Groupe selon le critère défini (pays)
country_grp.get_group('India') # Selectionne le groupe
country_grp['Employment'].value_counts() # Pour tous les pays
country_grp['Employment'].value_counts().loc['United States'] # Pour un seul pays

# Autres utilisation du groupby

country_grp['ConvertedComp'].median().loc['France']
country_grp['ConvertedComp'].agg(['median','mean']).loc['France']

# Combien de personnes utilise python en France : 
filt = df['Country'] == 'France'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').value_counts()

country_grp['LanguageWorkedWith'].apply(lambda x : x.str.contains('Python').sum()).loc['France'] # Car serie =/= serie de dataframe

#Combien de % de chaque pays connaissent python :

# Test rapide :
country_grp['LanguageWorkedWith'].apply(lambda x: (x.str.contains('Python').sum() / x.value_counts().sum()) * 100)

# Solution 1 : 

country_respondant = df['Country'].value_counts()
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x : x.str.contains('Python').sum())
python_df = pd.concat([country_respondant, country_uses_python], axis = 'columns', sort = False)
python_df.rename(columns = {'Country' : 'NumRespondants', 'LanguageWorkedWith' : 'NumKnowsPython'}, inplace = True)
python_df['PctKnowsPython'] = python_df['NumKnowsPython'] * 100/python_df['NumRespondants']
python_df.sort_values(by = 'PctKnowsPython', ascending=False, inplace = True)
