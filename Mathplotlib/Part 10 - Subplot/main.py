import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(("C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes-Python\\Mathplotlib\\Data\\data-salaries-dev.csv"))

plt.style.use('seaborn')

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


# Exemple 1 : Same
fig ,(ax1,ax2) = plt.subplots(nrows = 2, ncols = 1,sharex = True) # Two plots

# Exemple 2 : Différent window
# fig1, ax1 = plt.subplots() # Two plots
# fig2, ax2 = plt.subplots() # Two plots

ax1.plot(ages, py_salaries, label = 'Python')
ax2.plot(ages, js_salaries, label = 'JavaScript')

ax1.plot(ages, dev_salaries, color ='#444444', linestyle= '--', label = 'All devs')
ax2.plot(ages, dev_salaries, color ='#444444', linestyle= '--', label = 'All devs')

ax1.legend()
ax2.legend()

ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
