from point import *
import matplotlib as mpl
from matplotlib import pyplot as plt


# list of all splines to be displayed
splines = set()

# global variables
draggable_points = set()
selected_point = None

# max pixel distance from a point to be considered "on" the point
epsilon = 10

# graph parameters
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Spline Test')
    
def display():
    plt.show()

# removes a spline from being shown
# returns False if spline wasn't there to begin with
def remove_spline(spline):
    global splines

    if not spline in splines: return False
    
    splines.remove(spline)

    # TODO rest of function

    return True

def add_spline(spline, samples=10):
    global splines
    global draggable_points
    global epsilon

    # if spline is already being shown, redraw with new number of samples
    if spline in splines:
        remove_spline(spline)
    
    splines.add(spline)

    # plot control points of spline
    # plots points individually so that each one is a separate artist object
    draggable_points |= set(spline.control_points)
    for point in spline.control_points:
        plt.plot(point.x, point.y, 'o', color='k', picker=True, pickradius=epsilon)

    
    # plot curve of spline
    line = spline.sample(samples)
    xVals = [point.x for point in line]
    yVals = [point.y for point in line]
    plt.plot(xVals, yVals, 'b')

def onpick(event):
    global draggable_points
    global selected_point

    artist = event.artist
    x = artist.get_xdata()[0]
    y = artist.get_ydata()[0]
    for point in draggable_points:
        if x == point.x and y == point.y:
            selected_point = point
    print(selected_point)

fig.canvas.mpl_connect('pick_event', onpick)