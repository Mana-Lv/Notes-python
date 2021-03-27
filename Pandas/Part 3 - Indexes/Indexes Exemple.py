people = { 'First Name' : ["Futori", "Karlos", "Tom"],
            'Last Name' : ['Nama', "Roux", "Jill"],
            'Email' : ['MarieNama@email.fr', 'AlexRoux@email.fr', "TomJill@email.fr"]}

import pandas as pd 

df = pd.DataFrame(people)

print(df.set_index('Email', inplace = True)) # Définit le nouvel index, inplace conserve le changement

print(df)
print(df.loc['MarieNama@email.fr', 'Last Name'])
print(df.iloc[0])

df.reset_index(inplace = True) # Retablit les indexes numériques incrémenté
print(df)