# Simple exemple de compréhension 

# Serie : Array à une dimension
# Dataframe : Conteneur de plusieurs series (colonnes), 2 dimensions

people = { 'First Name' : ["Futori", "Karlos", "Tom"],
            'Last Name' : ['Nama', "Roux", "Jill"],
            'Email' : ['MarieNama@email.fr', 'AlexRoux@email.fr', "TomJill@email.fr"]}

import pandas as pd 

df = pd.DataFrame(people)

print(df)
print(type(df))
# Même logique mais plus d'option sur les dataframes

print(df['Email']) # Renvoie une serie (favori) on peut également utiliser la méthode suivante : print(df.Email)
# 
print(type(df['Email']))

print(df[['Last Name', 'Email']])

print(type(df.columns)) # Renvoie les nom des colonnes sous forme d'index

# Iloc : Integer location

print(df.iloc[0]) # Première ligne
print(df.iloc[[0, 1]]) # Deux premières lignes
print(df.iloc[[0, 1], 2]) # Email des deux premières lignes


# loc : Location
# [0,1,2] pareil que 0:2, attention aux crochets 
print(df.loc[[0, 1], ['Last Name','Email']]) # Deux premières lignes





