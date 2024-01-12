import math

def generate_points_on_diagonal(diameter, angle, n):
    radius = diameter / 2
    center = (0, 0)  # Assuming the center of the circle is at the origin

    # Calculate the coordinates of the center of the circle
    center_x, center_y = center

    # Calculate the angle between each equally spaced point
    delta_angle = math.radians(angle) / (n - 1)

    # Generate equally spaced points along the diagonal
    points = []
    for i in range(n):
        current_angle = delta_angle * i
        x = center_x + radius * math.cos(current_angle)
        y = center_y + radius * math.sin(current_angle)
        points.append((x, y))

    return points

# Example usage:
diameter = 300.0
angle = 0.0
num_points = 30

resulting_points = generate_points_on_diagonal(diameter, angle, num_points)

# Print the coordinates of the generated points
for point in resulting_points:
    print("Point:", point)
