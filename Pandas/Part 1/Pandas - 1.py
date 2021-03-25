import pandas as pd

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_public.csv")
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_schema.csv")

df.shape # return le couple (Rows, colomns)
df.info() # return les intitulés des colonnes, le nombre de non nul et le type

pd.set_option('display.max_columns', 5) # Définit le nombre max de colonnes
pd.set_option('display.max_rows', 5) # Définit le nombre max de ligne (row)

df.head(5) # Récupère les premières lignes
df.tail(5) # ... les dernières

print(schemas_df)