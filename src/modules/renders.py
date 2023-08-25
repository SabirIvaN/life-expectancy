from matplotlib import pyplot as plt

import seaborn as sns

def render_simple(obj_country, obj_name):
    plt.bar(obj_country, obj_name)
    plt.show()

def render_violin(obj, obj_x, obj_y, full_name):
    fig = plt.subplots(figsize=(15, 10)) 

    sns.violinplot(data = obj, x = obj_x, y = obj_y)

    plt.savefig(full_name + ".png")
    plt.show()

def render_bar(obj, type,  name):
    f, ax = plt.subplots(figsize=(10, 15))
    ax = sns.barplot(
        x = obj.Country,
        y = type,
        hue = obj.Year, 
        data = obj
    )

    plt.xticks(rotation= 90)
    plt.ylabel(name)
    plt.savefig(name + ".png")
    plt.show()

def render_scatter(obj, cols, heights, first_name, second_name, color, full_name):
    g = sns.FacetGrid(obj, col="Country", col_wrap=cols, height=heights)
    g = (g.map(plt.scatter, first_name, second_name, edgecolor=color).add_legend())

    plt.savefig(full_name + ".png")
    plt.show()

def render_line(obj, first_name, full_name):
    g = sns.FacetGrid(obj, col="Country", col_wrap=3, height=4)
    g = (g.map(plt.scatter, "Year", first_name).add_legend())
    plt.savefig(full_name + ".png")
    plt.show()