import gui
from bezier_curve import *

import numpy as np

gui.num_samples = 30

P1 = np.array([0., 0.])
P2 = np.array([0., 1.])
P3 = np.array([1., 1.])
P4 = np.array([1., 0.])

control_points = np.array([P1, P2, P3, P4])
spline = Bezier(control_points)
gui.add_spline(spline)
gui.display()