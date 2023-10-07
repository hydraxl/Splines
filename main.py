import gui
from bezier_curve import *
import numpy as np

gui.num_samples = 50

P1 = np.array([0.0, 0.0])
P2 = np.array([0.0, 0.5])
P3 = np.array([0.5, 0.0])
P4 = np.array([0.5, 0.5])
P5 = np.array([0.5, 1.0])
P6 = np.array([1.0, 0.5])
P7 = np.array([1.0, 1.0])


control_points_1 = np.array([P1, P2, P3, P4])
spline_1 = Bezier_Curve(control_points_1)

control_points_2 = np.array([P4, P5, P6, P7])
spline_2 = Bezier_Curve(control_points_2)
'''
control_points_3 = np.array([P1, P3, P2, P4])
spline_3 = Bezier_Curve(control_points_3)

control_points_4 = np.array([P4, P3, P1, P2])
spline_4 = Bezier_Curve(control_points_4)

control_points_5 = np.array([P2, P1, P4, P3])
spline_5 = Bezier_Curve(control_points_5)

control_points_6 = np.array([P3, P1, P2, P4])
spline_6 = Bezier_Curve(control_points_6)

control_points_7 = np.array([P2, P3, P4, P1])
spline_7 = Bezier_Curve(control_points_7)

control_points_8 = np.array([P2, P3, P1, P4])
spline_8 = Bezier_Curve(control_points_8)

control_points_9 = np.array([P2, P4, P3, P1])
spline_9 = Bezier_Curve(control_points_9)

control_points_10 = np.array([P1, P4, P2, P3])
spline_10 = Bezier_Curve(control_points_10)

control_points_11 = np.array([P3, P2, P1, P4])
spline_11 = Bezier_Curve(control_points_11)

control_points_12 = np.array([P3, P1, P2, P4])
spline_12 = Bezier_Curve(control_points_12)
'''

gui.add_spline(spline_1)
gui.add_spline(spline_2)
'''
gui.add_spline(spline_3)
gui.add_spline(spline_4)
gui.add_spline(spline_5)
gui.add_spline(spline_6)
gui.add_spline(spline_7)
gui.add_spline(spline_8)
gui.add_spline(spline_9)
gui.add_spline(spline_10)
gui.add_spline(spline_11)
gui.add_spline(spline_12)
'''
gui.display()
