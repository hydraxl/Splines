from point import *
from spline import *

class Bezier(Spline):
    # Uses repeated linear interpolation to sample n points along the curve
    def sample(self, n=10):
        line = []
        for i in range(n + 1):
            temp_points = []
            for p in range(len(self.control_points) - 1):
                new_point = (self.control_points[p] * (n - i) +  self.control_points[p + 1] * i) / n
                temp_points.append(new_point)
            
            while (len(temp_points) > 1):
                new_points = []
                for p in range(len(temp_points) - 1):
                    new_point = (temp_points[p] * (n - i) +  temp_points[p + 1] * i) / n
                    new_points.append(new_point)
                temp_points = new_points
            
            line.append(temp_points[0])
        
        return line