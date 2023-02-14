import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


print(os.getcwd())
os.chdir("C:/Users/aleja/Desktop/Bio-inspired-optimized-algorithms/plots/input")
print(os.getcwd())

gas = pd.read_csv('gas_prices.csv')
plt.figure(figsize=(8,5))

plt.title('Precios del gas a lo largo del tiempo (en USD)', fontdict={'fontweight':'bold', 'fontsize': 18})

plt.plot(gas.Year, gas.USA, 'b.-', label='Estados Unidos')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='Korea del Sur')
plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia' )
plt.plot(gas.Year, gas.Mexico, 'c.-', label='Mexico')

plt.xticks(gas.Year[::3].tolist()+[2008])

plt.xlabel('Año')
plt.ylabel('USD')

plt.legend()

plt.show()