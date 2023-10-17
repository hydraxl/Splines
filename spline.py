import numpy as np


# generic spline class only ever used as a parent class
# contains standard info and functions that every spline class must contain
class Spline:

    section_points = 1

    def __init__(self, control_points):
        self.control_points = control_points

    # generic spline doesn't exist, so sample returns empty list
    def sample(n=10):
        return np.empty(0)
    
    # adds new control points before the current set
    def add_front(self, new_points):
        if len(new_points) % self.section_points != 0:
            raise ValueError(f"Additions to this curve must have a multiple of {self.section_points} control points")
        self.control_points = new_points + self.control_points
    
    # adds new control points after the current set
    def add_back(self, new_points):
        if len(new_points) % self.section_points != 0:
            raise ValueError(f"Additions to this curve must have a multiple of {self.section_points} control points")
        self.control_points += new_points
