import pandas as pd 

people = { 'First Name' : ["Futori", "Karlos", "Tom"],
            'Last Name' : ['Nama', "Roux", "Jill"],
            'Email' : ['MarieNama@email.fr', 'AlexRoux@email.fr', "TomJill@email.fr"]}

df = pd.DataFrame(people)

filt = (df['Last Name'] == 'Jill') & (df['First Name'] == 'Tom') # Renvoie une serie de valeur avec True or False selon la condition
filt2 = df['Last Name'].isin(['Roux', 'Jill']) # Deuxième exemple de filtre 
print(df[filt]) # Pareil que  df.loc[filt]

a = df.loc[filt, 'Email']
b = df.loc[~filt, 'Email']

print(a , b)

# OR  :  |
# AND :  & 
# OPPOSITE : ~ avt le filtre

# Si on print un filtre, on a une liste de True/False values