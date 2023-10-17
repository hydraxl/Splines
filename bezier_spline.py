from spline import Spline
import numpy as np

class Bezier_Spline(Spline):

    # Number of control points needed to add a new section of curve
    section_points = 3

    # Sample n points in each section of the spline
    def sample(self, n=10):
        # Added for readability
        num_controls = len(self.control_points)

        # Each section should contain exactly 4 control points, one of which is shared with the previous section
        if (num_controls - 1) % self.section_points != 0:
            raise ValueError(f"Bezier Spline has {len(self.control_points)} control points, which is not one more than a multiple of {self.section_points}")
        
        # Setup variables
        num_sections = int((num_controls - 1) / self.section_points)
        line_length = (n * num_sections) + 1
        line = np.empty((line_length, 2))
        
        # Sample the spline
        for s in range(num_sections):
            section = self.control_points[s*self.section_points : (s+1)*self.section_points + 1]
            
            # Use linear interpolation to sample each bezier curve within the spline
            for i in range(n):

                # Create initial set of temporary points
                temp_points = np.empty((self.section_points, 2))
                for p in range(self.section_points):
                    new_point = (section[p] * (n - i) + section[p + 1] * i) / n
                    temp_points[p] = new_point

                # Create new temporary points from old temporary points until only 1 point remains
                while len(temp_points) > 1:
                    new_points = np.empty((len(temp_points) - 1, 2))
                    for p in range(len(temp_points) - 1):
                        new_point = (temp_points[p] * (n - i) + temp_points[p + 1] * i) / n
                        new_points[p] = new_point
                    temp_points = new_points
                
                # Add remaining point to the line
                line[i + s*n] = temp_points[0]
            
        # Final point on the line will always be the final control point
        line[len(line) - 1] = np.copy(self.control_points[num_controls - 1])

        return line





