import math

def generate_points_on_diagonal(diameter, angle, n):
    radius = diameter / 2
    center = (0, 0)  # Assuming the center of the circle is at the origin

    # Calculate the coordinates of the center of the circle
    center_x, center_y = center

    # Calculate the angle between each equally spaced point
    delta_angle = math.radians(angle) 
    
    minlen = diameter/(n-1)

    # Generate equally spaced points along the diagonal
    points = []
    
    current_angle = delta_angle 

    x = center_x + radius * math.cos(current_angle)
    y = center_y + radius * math.sin(current_angle)
    x = '{:.{}f}'.format(float(x), 4)
    y = '{:.{}f}'.format(float(y), 4)
    
    print(x,y)

    x = center_x - radius * math.cos(current_angle)
    y = center_y - radius * math.sin(current_angle)    
    x = '{:.{}f}'.format(float(x), 4)
    y = '{:.{}f}'.format(float(y), 4)
    x= float(x)
    y= float(y)
    print(x,y)
    points.append((x, y))
    
    for i in range(n-1):
        current_angle = delta_angle 
        x = x + minlen * math.cos(current_angle)
        y = y + minlen * math.sin(current_angle)
        
        x = '{:.{}f}'.format(float(x), 4)
        x = float(x) 
        y = '{:.{}f}'.format(float(y), 4)
        y = float(y)
        points.append((x, y))
        #print(x,y)
        #center_x = x
        #center_y = y

    return points

# Example usage:
diameter = 200.0
angle = 150.0
num_points = 31

f = open("demo3.txt", "w")

resulting_points = generate_points_on_diagonal(diameter, angle, num_points)
for i in resulting_points :
    f.write(str(i))
    f.write("\n")
    
f.close()

