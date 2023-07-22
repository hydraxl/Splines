from point import *
import matplotlib as mpl
from matplotlib import pyplot as plt

class GUI:
    def __init__(self):
        # list of all splines to be displayed
        self.splines = set()

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
    
    def display(self):
        plt.show()
    
    # removes a spline from being shown
    # returns False if spline wasn't there to begin with
    def remove_spline(self, spline):
        if not spline in self.splines: return False
        
        self.splines.remove(spline)

        # TODO rest of function

        return True
    
    def add_spline(self, spline, samples=10):
        # if spline is already being shown, redraw with new number of samples
        if spline in self.splines:
            self.remove_spline(spline)
        
        self.splines.add(spline)

        # plot control points of spline
        self.draggable_points |= set(spline.control_points)
        xVals = [point.x for point in spline.control_points]
        yVals = [point.y for point in spline.control_points]
        plt.plot(xVals, yVals, 'o', color='k', picker=True, pickradius=self.epsilon)
       
        # plot curve of spline
        line = spline.sample(samples)
        xVals = [point.x for point in line]
        yVals = [point.y for point in line]
        plt.plot(xVals, yVals, 'b')

    # TODO rest of GUI