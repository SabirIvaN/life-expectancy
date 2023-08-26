from matplotlib import pyplot as plt # Importing a package for drawing graphs from the library for data visualization

import os # Importing a library to work with the operating system

# Function to create files
def create_files(name, full_name):
    if (os.path.exists(name)):
        plt.savefig(name + "/" + full_name + ".png")
        plt.show()
    else:
        os.mkdir(name)
        plt.savefig(name + "/" + full_name + ".png")
        plt.show()
