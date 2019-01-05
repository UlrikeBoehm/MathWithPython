"""
A growing circle
"""

from matplotlib import pylab as plt
from matplotlib import animation

def create_circle():

    circle = plt.Circle((0,0), 0.05)
    return circle

def update_radius(i, circle):

    circle.radius = i*0.5
    return circle

def create_animation():

    fig = plt.gcf() # reference to the current figure
    ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(
        fig, update_radius, fargs = (circle,), frames=30, interval=50) # repeat=False -> it will only once
    plt.title('Simple Circle Animation')
    plt.show()

if __name__ == '__main__':

    create_animation()