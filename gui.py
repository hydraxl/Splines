import matplotlib as mpl
from matplotlib import pyplot as plt

# initialization parameters for graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Spline Test')

# plots points with lines connecting them
def plot_lines(points):
    xVals = [point.x for point in points]
    yVals = [point.y for point in points]
    plt.plot(xVals, yVals, 'b', color='k')

# plots points as dots
def plot_points(points):
    xVals = [point.x for point in points]
    yVals = [point.y for point in points]
    plt.plot(xVals, yVals, 'o', color='k')

def display():
    plt.show()