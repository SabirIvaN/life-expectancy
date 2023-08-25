from matplotlib import pyplot as plt

import seaborn as sns
import pandas as pd
import os

from modules.settings import rename_column

from modules.renders import render_simple
from modules.renders import render_violin
from modules.renders import render_bar
from modules.renders import render_scatter
from modules.renders import render_line

# Read in the data
file_path = os.getcwd() + "/src/database/data.csv"
df = pd.read_csv(file_path)

# Doing a slight rename for one of the columns.
rename_column(df)

# Bar Charts To Compare Average

# First high level look
render_simple(df.Country, df.GDP)

# Violin Plots To Compare Life Expectancy Distributions
render_violin(df, df.Country, df.LEABY, "violinplot")

# Bar Plots Of GDP and Life Expectancy over time
render_bar(df, df.GDP, "GDP in Trillions of U.S. Dollars")
render_bar(df, df.LEABY, "Life expectancy at birth in years")

# Scatter Plots of GDP and Life Expectancy Data
render_scatter(df, 4, 2, "GDP", "LEABY", "w", "GDP vs LEABY")

# Line Plots for Life Expectancy
render_line(df, "LEABY", "LEABY Comparision")

# Line Plots for GDP
render_line(df, "GDP", "GDP comparision")
