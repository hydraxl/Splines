# Stores the location of a point in 2d space
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # treats point as a vector for the purpose of mathematical operations
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, n):
        return Point(self.x * n, self.y * n)
    
    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)


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