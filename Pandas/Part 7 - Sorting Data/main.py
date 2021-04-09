import pandas as pd
import math

df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_public.csv"
                , index_col = 'Respondent')
schemas_df = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-python\\Pandas\\data\\survey_results_schema.csv"
                        , index_col = 'Column')

# Par pays puis salaire décroissant  :

df.rename(columns = { 'ConvertedComp' : 'SalaryUSD'}, inplace = True)
df2 = df[['Country','SalaryUSD']].sort_values(by = ['Country','SalaryUSD'], ascending = [True, False])

def isNotNaN(num):
    return num == num

df2['Country']

filter_NaN = isNaN(df2['Country'])

df2.loc[filter_NaN]