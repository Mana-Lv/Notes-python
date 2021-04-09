import pandas as pd

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_public.csv")
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_schema.csv")

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(df.shape)
print(df.columns)

print(df['Hobbyist'])
print(df['Hobbyist'].value_counts())

print(df.loc[0:2, 'Hobbyist'] # identique à df.loc[[0,1,2], ('Hobbyist')]