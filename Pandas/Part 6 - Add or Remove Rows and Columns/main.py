import pandas as pd

people =  {"First" : ['Alex', 'Tom', 'Maxime'],
        "Age" : [26, 28, 30], 
        "email" : ["Exemple1@mail.com", "Exemple2@mail.com", "Exemple3@mail.com" ]}

df = pd.DataFrame(people)

df['name_email'] = df['First'] + ' ' + df['email'] # Création d'une nouvelle colonne
df.drop(columns=["First", "email"], inplace = True)

# Take back the old columns

df[['First','email']] = df["name_email"].str.split(' ', expand = True)

df.append({'First' : 'Tony'}, ignore_index = True) # Attention ne conserve pas les modifications, on remarque la création d'une LIGNE

people = {
        'First' :  ['Nass', 'Jill'],
        'Age' : [26,28],
        'email' : ['Exemple4@mail.com','Exemple5@mail.com']
}

df2 = pd.DataFrame(people)
df = df.append(df2, ignore_index=True) # Pour concerver les modifications


df = df.drop(index = 3)

df.drop(index = df[df['First'] == 'Jill'].index) # Conditionnel

# En externalisant la contrainte, pour plus de lisibilité
filt = df['First'] == 'Jill'
df.drop(index = df[filt].index)

