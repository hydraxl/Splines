import gui
from bezier_curve import *
import numpy as np

gui.num_samples = 50

P1 = np.array([0.0, 0.0])
P2 = np.array([0.0, 1.0])
P3 = np.array([1.0, 1.0])
P4 = np.array([1.0, 0.0])

control_points_1 = np.array([P1, P2, P3, P4])
spline_1 = Bezier(control_points_1)
control_points_2 = np.array([P1, P3, P2, P4])
spline_2 = Bezier(control_points_2)

gui.add_spline(spline_1)
gui.add_spline(spline_2)
gui.display()
