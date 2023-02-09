import pandas as pd;
import os;
import matplotlib.pyplot as plt;
from matplotlib.animation import FuncAnimation;
import numpy;
from itertools import count;

print(os.getcwd())
os.chdir("C:/Users/aleja/Desktop/Bio-inspired-optimized-algorithms/plots/input")
print(os.getcwd())

data=pd.read_csv(r"201-300-ejemplo.csv")

df=pd.DataFrame(data)

df1=(df["Country"].value_counts())/len(df["Country"])*100

plt.xticks(rotation=45)
plt.ylabel("Percent")
df1.plot(kind="bar")

plt.show()