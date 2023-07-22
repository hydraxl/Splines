from point import *
import matplotlib as mpl
from matplotlib import pyplot as plt

# global variables
draggable_points = set()

# max pixel distance from a point to be considered "on" the point
epsilon = 10

mousePressed = False
mouseX = 0
mouseY = 0

# initialization parameters for graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Spline Test')

# plots points with lines connecting them
def plot_lines(points):
    xVals = [point.x for point in points]
    yVals = [point.y for point in points]
    plt.plot(xVals, yVals, 'b')

# plots points as dots
def plot_points(points):
    global draggable_points
    draggable_points |= set(points)
    
    xVals = [point.x for point in points]
    yVals = [point.y for point in points]
    plt.plot(xVals, yVals, 'o', color='k', picker=True, pickradius=epsilon)

def display():
    plt.show()

def button_press_callback(event):
    global draggable_points
    'Whenever a mouse button is pressed'
    mousePressed = True
    mouseX = event.x
    mouseY = event.y

def button_release_callback(event):
    'Whenever a mouse button is released'

def motion_notify_callback(event):
    'On mouse movement'

fig.canvas.mpl_connect('button_press_event', button_press_callback)