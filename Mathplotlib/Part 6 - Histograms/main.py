# A utiliser lorsque l'on a beaucoup de valeurs différentes

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

"""
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [20, 30, 40, 50, 60] # Possible d'utiliser une valeur unique mais moins lisible

plt.hist(ages, bins = bins, edgecolor = 'b')
"""

data = pd.read_csv('C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Mathplotlib\\Data\\data-ages.csv')
ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#FC4F30'

plt.axvline(median_age, color = color, label = "Age Median", linewidth = 2)

print(ids)
ages

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins = bins, edgecolor='black', color = 'blue', log = True)
# La méthode log permet d'avoir une meilleure visibilité grace au log

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Responents')

plt.tight_layout()

plt.show()
