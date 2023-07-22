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