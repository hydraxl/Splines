from point import *

# Uses nested linear interpolation to create a bezier curve
# Takes in a list of control points
# Outputs a list of points along the bezier curve
def bezier_lerp(points, steps=10):
    line = []
    for i in range(steps + 1):
        temp_points = []
        for p in range(len(points) - 1):
            temp_points.append((points[p] * (steps - i) +  points[p + 1] * i) / steps)
        
        while (len(temp_points) > 1):
            new_points = []
            for p in range(len(temp_points) - 1):
                new_points.append((temp_points[p] * (steps - i) +  temp_points[p + 1] * i) / steps)
            temp_points = new_points
        
        line.append(temp_points[0])
    
    return line