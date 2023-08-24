from matplotlib import pyplot as plt

import seaborn as sns
import pandas as pd
import os

# Read in the data
file_path = os.getcwd() + "/src/database/data.csv"
df = pd.read_csv(file_path)

# Doing a slight rename for one of the columns. It has a very long time which is good for labeling, but not so nice for using in a plot. After that, the renaming check is performed.
df.rename(columns= {"Life expectancy at birth (years)" : "LEABY"}, inplace= True)
df.head()

# Bar Charts To Compare Average

# First high level look
plt.bar(df.Country, df.GDP)
plt.show()

# Violin Plots To Compare Life Expectancy Distributions 

fig = plt.subplots(figsize=(15, 10)) 

sns.violinplot(data = df, x = df.Country, y = df.LEABY)

plt.savefig("violinplot.png")
plt.show()

# Bar Plots Of GDP and Life Expectancy over time

f, ax = plt.subplots(figsize=(10, 15))
ax = sns.barplot(
    x = df.Country,
    y = df.GDP,
    hue = df.Year, 
    data = df
)

plt.xticks(rotation= 90)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.show()

f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(
    x = df.Country,
    y = df.LEABY,
    hue = df.Year, 
    data = df
)

plt.xticks(rotation= 90)
plt.ylabel("Life expectancy at birth in years")
plt.savefig("Life expectancy at birth in years")
plt.show()

# Scatter Plots of GDP and Life Expectancy Data

g = sns.FacetGrid(df, col="Country", hue="Year", col_wrap=4, height=2)
g = (g.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend())

plt.savefig("GDP vs LEABY.png")
plt.show()

# Line Plots for Life Expectancy

g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.scatter, "Year", "LEABY").add_legend())
plt.savefig("LEABY Comparision.png")
plt.show()

# Line Plots for GDP

g4 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g4 = (g4.map(plt.scatter, "Year", "GDP").add_legend())
plt.savefig("GDP comparision.png")
plt.show()

