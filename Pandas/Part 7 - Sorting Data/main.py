import pandas as pd
import math

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_public.csv"
                , index_col = 'Respondent')
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_schema.csv"
                        , index_col = 'Column')

# Par pays puis salaire décroissant  :

df.rename(columns = { 'ConvertedComp' : 'SalaryUSD'}, inplace = True)
df2 = df[['Country','SalaryUSD']].sort_values(by = ['Country','SalaryUSD'], ascending = [True, False])

# Permets d'enlever les valeurs NaN

def isNotNaN(num):
    return num == num

df2['Country']

filter_NaN = isNotNaN(df2['Country'])
filter_NaN2 = isNotNaN(df2['SalaryUSD'])

df2 = df2.loc[filter_NaN]
df2 = df2.loc[filter_NaN2]

df2.head(50)

# Autres méthodes : 

df['SalaryUSD'].nlargest(10) # Récupère les 10 plus grandes valeurs
df.nlargest(10, 'SalaryUSD') # .. Avec le reste des infos 
df.nsmallest(10, 'SalaryUSD') # .. Méthode inversée

