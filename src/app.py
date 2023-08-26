#!/usr/bin/env python3

import pandas as pd # Import Library for Data Analysis
import os # Importing a library to work with the operating system

from modules.settings import rename_column # Import from the settings module of the function of renaming columns
from modules.renders import render_scatter # Import from the renderer module of the scatter chart drawing function
from modules.renders import render_simple # Importing a simple graph drawing function from the renderer module
from modules.renders import render_violin # Import from the renderer module of the violin graph drawing function
from modules.renders import render_bar # Import from the renderer module of the bar chart drawing function

# Read in the data
file_path = os.getcwd() + "/src/database/data.csv"
df = pd.read_csv(file_path)

# Doing a slight rename for one of the columns
rename_column(df)

# Bar Charts To Compare Average

# First high level look
render_simple(df.Country, df.GDP)

# Violin Plots To Compare Life Expectancy Distributions
render_violin(df, df.Country, df.LEABY, "Violinplot")

# Bar Plots Of GDP and Life Expectancy over time
render_bar(df, df.GDP, "GDP in Trillions of U.S. Dollars")
render_bar(df, df.LEABY, "Life expectancy at birth in years")

# Scatter Plots of GDP and Life Expectancy Data, Line Plots for Life and Plots Expectancy and Line Plots for GDP
render_scatter(df, 4, 2, "GDP", "GDP vs LEABY", "LEABY", "w")
render_scatter(df, 3, 4, "LEABY", "LEABY Comparision")
render_scatter(df, 3, 4, "GDP", "GDP comparision")
