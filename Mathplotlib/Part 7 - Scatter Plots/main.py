# Voir les correlations entre les datas

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

""" Sample data
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

plt.scatter(x, y, s = 100, c = colors, cmap = 'Greens', edgecolors='black', linewidth = 1, alpha = 0.75) # Autres options : Marker, alpha (transparance), Edgecolor

cbar = plt.colorbar() 
cbar.set_label('Satisfaction')
"""

data = pd.read_csv("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-Python\\Mathplotlib\\Data\\youtube-viewratio.csv")
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# lisse les différences avec log en cas de valeur isolée 
plt.xscale('log')
plt.yscale('log')

plt.scatter(x = view_count, y = likes, edgecolors= 'black', linewidth = 1, c = ratio, cmap = "summer")

cbar = plt.colorbar()
cbar.set_label('Likes/Dislike Ratio')

plt.legend()
plt.tight_layout()
plt.show()
