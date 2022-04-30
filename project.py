import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
europe = ["France", "Italy", "Spain", "Finland", "Germany", "Belgium"]
nas = ["Brazil", "Chile", "United States", "Canada", "Cuba", "Argentina"]
asia = ["China", "India", "Japan", "Vietnam", "Indonesia", "Israel"]
df = pd.read_csv("bmsd.csv", header=0)
unique_countries = df['name'].unique()
for c in unique_countries:
  if c in asia:
    years = df[df['name'] == c]['Year']
    price =(df[df['name'] == c]['Price']).astype(np.float)

    plt.plot(years, price, label=c, linestyle = ":")
  plt.ylabel('Price of a Big Mac')
plt.xlabel('Year')
plt.title('Historical Price of a Big Mac across Time')
plt.legend()
plt.show()
