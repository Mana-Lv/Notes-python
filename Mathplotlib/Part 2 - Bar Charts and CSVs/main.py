from matplotlib import pyplot as plt
import numpy as np

from collections import Counter

# CSV
import csv
with open('C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Mathplotlib\\Part 2 - Bar Charts and CSVs\\data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # row = next(csv_reader) # Première ligne

    language_counter = Counter()

    for row in csv_reader: 
        language_counter.update(row['LanguagesWorkedWith'].split(";"))

#Pandas

"""
import pandas as pd
data = pd.read_csv('C:\\Users\\Al120\\Desktop\\Programmation\\Github\\Notes python\\Mathplotlib\\Part 2 - Bar Charts and CSVs\\data.csv')
print(data["LanguagesWorkedWith"])

c = Counter()

for item in data["LanguagesWorkedWith"]:
    c.update(item.split(";"))
"""


languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity, color = "#5A7D9A") # barh =>  Vertical bar chart

plt.title("Most popular languages")

plt.xlabel("Number of people using")

plt.legend()

plt.tight_layout()
plt.show()
