import gui
from point import *
from bezier_curve import *

import numpy as np

P1 = Point(0, 0)
P2 = Point(0, 1)
P3 = Point(1, 1)
P4 = Point(1, 0)

control_points = np.array([P1, P2, P3, P4])
spline = Bezier(control_points)

gui.add_spline(spline, samples=30)
gui.display()