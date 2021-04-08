from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("seaborn")

# Paramètre usuel pour le plot : color, linestyle, marker, label, linewidth

# Donne un DataFrame avec les données CSV
data = pd.read_csv('C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Mathplotlib\\Data\\data-salaries-dev.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, py_salaries, color= '#ADAD3B', label = 'Python Devs')
plt.plot(ages, dev_salaries, color= '#444444', linestyle =  '--', label = 'All Devs')

# Fill classique entre un jeu de donnée et 0
#plt.fill_between(ages, y1 = py_salaries, alpha = 0.25)

# ... Avec une constante arbitraire par exemple et avec condition
# overall_median = 57287
# plt.fill_between(ages, y1 = py_salaries, y2 = overall_median, where = (py_salaries > overall_median), interpolate = True, color = 'g', alpha = 0.25)
# plt.fill_between(ages, y1 = py_salaries, y2 = overall_median, where = (py_salaries <= overall_median), interpolate = True, color = "r", alpha = 0.25)

# Avec une autre courbe ! 
plt.fill_between(ages, y1 = py_salaries, y2 = dev_salaries, where = (py_salaries > dev_salaries), interpolate = True, color = 'g', alpha = 0.25, label = "Above Avg.")
plt.fill_between(ages, y1 = py_salaries, y2 = dev_salaries, where = (py_salaries <= dev_salaries), interpolate = True, color = "r", alpha = 0.25, label = "Below Avg.")

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.grid(True)
plt.tight_layout()

plt.show()

