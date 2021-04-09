import pandas as pd

people = {
    'first' : ['Alex','Tom','Maxime','Bernard'],
    'last' : ['Ou', 'la', 'la', 'la'],
    'age' : [26,46,30,32]
}

df = pd.DataFrame(people)

df.sort_values(by = 'last', ascending = False) # Méthode basique

df.sort_values(by = ['last', 'first'], ascending = False) # Possible de faire plusieurs tris
df.sort_values(by = ['last', 'first'], ascending = [False,True]) # Possible de faire un tri croissant selon les critères

df.sort_index(ascending = False) # Par index

df['last'].sort_values() # Sur une colonne