import poorly_designed_but_working_gui as gui
from point import *
from bezier_curve import *

P1 = Point(0, 0)
P2 = Point(0, 1)
P3 = Point(1, 1)
P4 = Point(1, 0)
control_points = [P1, P2, P3, P4]

spline = Bezier(control_points)

samples = spline.sample(30)

gui.plot_lines(samples)
gui.plot_points(control_points)

gui.display()