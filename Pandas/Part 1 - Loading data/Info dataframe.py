import pandas as pd

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_public.csv"
                , index_col = 'Respondent')
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Pandas\\data\\survey_results_schema.csv"
                        , index_col = 'Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(df.info())
