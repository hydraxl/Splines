import numpy as np


# generic spline class only ever used as a parent class
# contains standard info and functions that every spline class must contain
class Spline:
    def __init__(self, control_points):
        self.control_points = control_points

    # generic spline doesn't exist, so sample returns empty list
    def sample(n=10):
        return np.empty(0)
    
    # adds new control points before the current set
    def add_front(self, new_points):
        self.control_points = new_points + self.control_points
    
    # adds new control points after the current set
    def add_back(self, new_points):
        self.control_points += new_points
