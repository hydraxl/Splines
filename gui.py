from point import *
import matplotlib as mpl
from matplotlib import pyplot as plt

class gui:
    def __init__(self, splines=[]):
        # list of all splines to be displayed
        self.splines = splines

        # global variables
        self.draggable_points = set()

        # max pixel distance from a point to be considered "on" the point
        self.epsilon = 10

        # graph parameters
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Spline Test')
    
    # TODO create actual GUI