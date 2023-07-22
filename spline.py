from point import *

# generic spline class only ever used as a parent class
# contains standard info and functions that every spline class must contain
class Spline:
    def __init__(self, control_points):
        self.control_points = control_points
    
    # generic spline doesn't exist, so sample returns empty list
    def sample(n=10):
        return []