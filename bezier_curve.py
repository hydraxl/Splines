from spline import *

import numpy as np

class Bezier(Spline):
    # Uses repeated linear interpolation to sample n points along the curve
    # Computationally inefficient method, will be replaced later
    def sample(self, n=10):
        line = np.empty((n + 1, 2))
        for i in range(n + 1):
            
            temp_points = np.empty((len(self.control_points) - 1, 2))
            for p in range(len(self.control_points) - 1):
                new_point = (self.control_points[p] * (n - i) +  self.control_points[p + 1] * i) / n
                temp_points[p] = new_point
            
            while (len(temp_points) > 1):
                new_points = np.empty((len(temp_points) - 1, 2))
                for p in range(len(temp_points) - 1):
                    new_point = (temp_points[p] * (n - i) +  temp_points[p + 1] * i) / n
                    new_points[p] = new_point
                temp_points = new_points
            
            line[i] = temp_points[0]
        
        return line