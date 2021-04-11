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
df['Hobbyist'].value_counts(normalize = True) # Compte selon la réponse, avec l'option normalize, donne en %

df['DevType']

