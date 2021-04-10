import pandas as pd
import random
from itertools import count
import matplotlib.pyplot as plt
import matplotlib.animation as ani

plt.style.use('seaborn')

index = count()

"""
x_vals = []
y_vals = []

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))

    plt.cla() # Clear the current axe
    plt.plot(x_vals, y_vals)
"""

def animate(i):

    data = pd.read_csv('C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-Python\\Mathplotlib\\Data\\data_generated.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x, y1, label = 'Karma M')
    plt.plot(x, y2, label = 'Karma A')

    plt.legend(loc = 'upper left')

ani = ani.FuncAnimation(plt.gcf(), animate, interval=1000) # gcf = getCurrentFigure, interval in ms not s


plt.tight_layout()
plt.show()