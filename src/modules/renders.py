from matplotlib import pyplot as plt # Importing a package for drawing graphs from the library for data visualization

import seaborn as sns # Import library to create a graph

# Drawing a simple graph
def render_simple(obj_country, obj_name):
    plt.bar(obj_country, obj_name)
    plt.show()

# Draw violin graphics
def render_violin(obj, obj_x, obj_y, full_name):
    plt.subplots(figsize=(15, 10))

    sns.violinplot(
        data = obj, 
        x = obj_x, 
        y = obj_y
    )

    plt.savefig(full_name + ".png")
    plt.show()

# Drawing bar chart
def render_bar(obj, type,  name):
    plt.subplots(figsize=(10, 15))

    sns.barplot(
        x = obj.Country,
        y = type,
        hue = obj.Year, 
        data = obj
    )

    plt.xticks(rotation= 90)
    plt.ylabel(name)
    plt.savefig(name + ".png")
    plt.show()

# Draw scatter chart
def render_scatter(obj, cols, heights, first_name, full_name, second_name = None, color = None):
    g = sns.FacetGrid(obj, col = "Country", col_wrap = cols, height = heights)
    
    if ((second_name == None) and (color == None)):
        g = (g.map(plt.scatter, "Year", first_name).add_legend())
    else:
        g = (g.map(plt.scatter, first_name, second_name, edgecolor = color).add_legend())

    plt.savefig(full_name + ".png")
    plt.show()
