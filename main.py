import gui
import bezier_curve as bc

P1 = bc.Point(0, 0)
P2 = bc.Point(0, 1)
P3 = bc.Point(1, 1)
P4 = bc.Point(1, 0)
control_points = [P1, P2, P3, P4]

curve = bc.bezier_lerp(control_points, 30)

gui.plot_lines(curve)
gui.plot_points(control_points)

gui.display()