import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

print(os.getcwd())
os.chdir("C:/Users/aleja/Desktop/Bio-inspired-optimized-algorithms/plots/input")
print(os.getcwd())

fifa = pd.read_csv('fifa_data.csv')

bins = [40,50,60,70,80,90,100]

plt.figure(figsize=(8,5))

plt.hist(fifa.Overall, bins=bins, color='#abcdef')

plt.xticks(bins)

plt.ylabel('Número de jugadores')
plt.xlabel('Nivel de habilidad')
plt.title('Distribución de las habilidades de los jugadores en FIFA 2018')

plt.show()