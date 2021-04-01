import pandas as pd

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_public.csv"
                , index_col = 'Respondent')
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_schema.csv"
                        , index_col = 'Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.rename(columns= {'ConvertedComp' : 'SalaryUSD'}, inplace = True)

high_salary = (df['SalaryUSD'].isnull())
df[~high_salary]['SalaryUSD'] # Récupère les valeurs non nulles


df['Hobbyist'] = df['Hobbyist'].map({'Yes' : True, 'No': False})
df[['Hobbyist', 'SalaryUSD']].info()

df['Age1stCode'] = pd.to_numeric(df['Age1stCode'],errors='coerce')
# https://qastack.fr/programming/15891038/change-data-type-of-columns-in-pandas

age1st = (df['Age1stCode'].isnull())
df[~age1st]['Age1stCode'].mean() # Moyenne d'âge du premier code