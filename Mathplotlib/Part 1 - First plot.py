from matplotlib import pyplot as plt

plt.style.use("seaborn")

# Paramètre usuel pour le plot : color, linestyle, marker, label, linewidth
age_x = [25,26,27,28,29,30,31,32,33,34,35]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(age_x, py_dev_y, color = '#5A7D9A' , label='Python', linewidth = 2)

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(age_x, js_dev_y, color = '#ADAD3B' , label='JS')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(age_x, dev_y,  color = 'k', linestyle = "--" , marker = '.' , label='All Devs')

plt.title('Median Salary (USD) by Age')

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# plt.legend(['All Devs', 'Python']) # Première méthode dans l'ordre des plots
plt.legend() # Méthode de légende avec les label des plots

plt.grid(True)
plt.tight_layout()


plt.show()

