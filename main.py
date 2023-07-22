import gui
from point import *
from bezier_curve import *

P1 = Point(0, 0)
P2 = Point(0, 1)
P3 = Point(1, 1)
P4 = Point(1, 0)
control_points = [P1, P2, P3, P4]

curve = Bezier(control_points)

curve_samples = curve.sample(30)

gui.plot_lines(curve_samples)
gui.plot_points(control_points)

gui.display()