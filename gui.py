from point import *
import matplotlib as mpl
from matplotlib import pyplot as plt


# list of all splines to be displayed
splines = set()

# global variables
draggable_points = {} # Follows the format { Point : [Artist, (Spline, Artist), (Spline, Artist), ...]}
selected_point = None
num_samples=10

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


def add_spline(spline):
    global splines
    global draggable_points

    splines.add(spline)

    # plot curve of spline
    curve = spline.sample(num_samples)
    xVals = [point.x for point in curve]
    yVals = [point.y for point in curve]
    curve_artist, = plt.plot(xVals, yVals, 'b')

    # plot control points of spline
    # plots points individually so that each one is a separate artist object
    for point in spline.control_points:
        if not point in draggable_points:
            point_artist, = plt.plot(point.x, point.y, 'o', color='k', picker=True, pickradius=epsilon)
            draggable_points[point] = [point_artist]            
        draggable_points[point].append((spline, curve_artist))

# Whenever an artist object is clicked on
def onpick(event):
    global draggable_points
    global selected_point

    artist = event.artist
    x = artist.get_xdata()[0]
    y = artist.get_ydata()[0]
    for point in draggable_points.keys():
        if point.x == x and point.y == y:
            selected_point = point

# Whenever the mouse button is released
def onrelease(event):
    global selected_point
    selected_point = None

# Whenever the mouse moves
def onmotion(event):
    global selected_point
    
    if selected_point is None: return
    
    draggable_points[selected_point][0].set_xdata(event.xdata)
    draggable_points[selected_point][0].set_ydata(event.ydata)

    selected_point.x = event.xdata
    selected_point.y = event.ydata
    
    for spline, artist in draggable_points[selected_point][1:]:
        curve = spline.sample(num_samples)
        artist.set_xdata([point.x for point in curve])
        artist.set_ydata([point.y for point in curve])

    fig.canvas.draw_idle()
        

fig.canvas.mpl_connect('pick_event', onpick)
fig.canvas.mpl_connect('button_release_event', onrelease)
fig.canvas.mpl_connect('motion_notify_event', onmotion)