import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

print(os.getcwd())
os.chdir("C:/Users/aleja/Desktop/Bio-inspired-optimized-algorithms/plots/input")
print(os.getcwd())

fifa = pd.read_csv('fifa_data.csv')

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

plt.figure(figsize=(8,5))

labels = ['Izquierdo', 'Derecho']
colors = ['#abcdef', '#aabbcc']

plt.pie([left, right], labels = labels, colors=colors, autopct='%.2f %%')

plt.title('Preferencia de pie de los jugadores de la FIFA')

plt.show()