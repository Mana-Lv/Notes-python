from matplotlib import pyplot as plt 

plt.style.use("seaborn")
""" 
First exemple
slices = [60, 40, 15, 10]
labels = ['Sixty','Forty', 'Extra1', 'Extra2']
colors = ['#008FD5','#FC4F30','#E5AE37','#6D904F'] # Add parameter color
"""

slices = [59219, 55466, 47544, 36443, 35917] 
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0] # Emphasize by separating

plt.pie(slices, labels=labels, explode = explode, shadow = True, startangle=90, autopct = '%1.1f%%',
    wedgeprops = {'edgecolor': 'black'})

plt.title("Awesom Pie Chart")
plt.tight_layout()
plt.show()

