import pandas as pd

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_public.csv"
                , index_col = 'Respondent')
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_schema.csv"
                        , index_col = 'Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)



high_salary = (df['ConvertedComp'] > 70000)
filt_python = df['LanguageWorkedWith'].str.contains('Python', na = False)

#print(df.loc[high_salary, ['Country', 'Trans', 'ConvertedComp', 'Age1stCode']])
print(df.loc[filt_python, ['Age','LanguageWorkedWith', 'ConvertedComp']])