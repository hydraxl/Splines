import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np


# list of all splines to be displayed
splines = set()

# global variables
draggable_points = []
draggable_point_info = [] # Follows the format [[Artist, (Spline, Artist), (Spline, Artist), ...], ...]
selected_point_index = None
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
    global draggable_point_info

    splines.add(spline)

    # plot curve of spline
    curve = spline.sample(num_samples)
    xVals = [point[0] for point in curve]
    yVals = [point[1] for point in curve]
    curve_artist, = plt.plot(xVals, yVals, 'b')

    # plot control points of spline
    # plots points individually so that each one is a separate artist object
    for point in spline.control_points:
        # if point is already plotted, find it in draggable_points
        index = None
        for i in range(len(draggable_points)):
            if draggable_points[i][0] == point[0] and draggable_points[i][1] == point[1]:
                index = i
                break
        
        # if point isn't plotted, plot it and add it to draggable_points
        if index is None:
            point_artist, = plt.plot(point[0], point[1], 'o', color='k', picker=True, pickradius=epsilon)
            draggable_points.append(point)
            draggable_point_info.append([point_artist])
            index = len(draggable_points) - 1
        
        # add spline to draggable_point_info
        draggable_point_info[index].append((spline, curve_artist))

# Whenever an artist object is clicked on
def onpick(event):
    global draggable_points
    global selected_point_index

    artist = event.artist
    x = artist.get_xdata()[0]
    y = artist.get_ydata()[0]
    for i in range(len(draggable_points)):
        point = draggable_points[i]
        if point[0] == x and point[1] == y:
            selected_point_index = i

# Whenever the mouse button is released
def onrelease(event):
    global selected_point
    global selected_point_index
    selected_point = None
    selected_point_index = None

# Whenever the mouse moves
def onmotion(event):
    global selected_point_index
    
    if selected_point_index is None: return
    
    # change position of point
    draggable_points[selected_point_index][0] = event.xdata
    draggable_points[selected_point_index][1] = event.ydata

    # re-plot point
    draggable_point_info[selected_point_index][0].set_xdata(event.xdata)
    draggable_point_info[selected_point_index][0].set_ydata(event.ydata)
    
    # re-plot splines that use point
    for spline, artist in draggable_point_info[selected_point_index][1:]:
        curve = spline.sample(num_samples)
        artist.set_xdata([point[0] for point in curve])
        artist.set_ydata([point[1] for point in curve])

    fig.canvas.draw_idle()
        

fig.canvas.mpl_connect('pick_event', onpick)
fig.canvas.mpl_connect('button_release_event', onrelease)
fig.canvas.mpl_connect('motion_notify_event', onmotion)