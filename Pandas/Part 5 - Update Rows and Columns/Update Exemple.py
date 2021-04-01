import pandas as pd

people =  {"First" : ['Alex', 'Tom', 'Maxime'],
        "Age" : [26, 28, 30], 
        "email" : ["Exemple1@mail.com", "Exemple2@mail.com", "Exemple3@mail.com" ]}

df = pd.DataFrame(people)

# Travail sur les colonnes 

df.columns # Récupère len nom des colonnes

df.columns = ['First_name', 'Age_test', 'email'] # Définir le nom des colonnes à l'aide d'une liste 

df.columns # Les colonnes ont changés 

df.columns = [x.lower() for x in df.columns] # Change le nom des colonnes en minuscule
df.columns = df.columns.str.replace("_", " ") # Ne marche pas mais plus 

# Autre méthode : rename
df.rename(columns={'first name' : 'first', 'age test' : 'age'}, inplace = True) # Inplace permet de conserver les changements 


# Travail sur une lignes loc/at or iloc

df.loc[2] = ['Maxime',32,"MaximeExemple@mail.com"]
df.loc[2, ['age','email']] = [33, 'Exemple3@mail.com'] # Pour changer seulement certains éléments du df
df.loc[2, 'email'] = ['Exemple3modif@mail.com'] # ... Avec un seul élément par exemple 

# Exemples de travail sur l'ensemble des lignes

df['email'].str.lower()
df['email'].str.replace('mail.com', 'yahoo.fr')

# Travail plus ciblé avec les fonction apply/lambda

df['email'].apply(len) # Permets d'avoir des informations sur nos datas en appliquant une fonction, le nombre de caractère de chaque email
df.apply(len) # Le nombre de lignes

def update_email(email):
    return email.upper()

df['email'].apply(update_email) #... Fonction personalisée également

df['email'] = df['email'].apply(update_email) # Pour changer les valeurs du df
df['email'] = df['email'].apply(lambda x : x.lower())

df['first'].apply(str.lower)

df.apply(pd.Series.min) #Récupère les valeurs minimum, par ordre alphabétique ou croissant pour les nombres 
df.apply(lambda x : x.min())  # Pareil avec une utilisation de la fonction lambda
df.min() # plus simplement ..

df.applymap(len) # Applique la fonction à tous les éléments

df['first'] = df['first'].map({'Alex' : 'Alan', 'Tom' : 'Mateo'}) # Les valeurs non prise en compte par la méthode map sont transformée en NaN, utiliser replace si on veut conserver les anciennes valeurs non préçisées
df.loc[2,'first'] = 'John'

