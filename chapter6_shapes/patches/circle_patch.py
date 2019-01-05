"""
Example of using matplotlib's Circle patch
"""

import matplotlib.pyplot as plt

def create_circle():

    circle = plt.Circle((0,0), radius = 0.5)
    return circle

def show_shape(patch):

    ax = plt.gca() # returns a reference to the current Axes
    ax.set_aspect('equal')
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':

    c = create_circle()
    show_shape(c)