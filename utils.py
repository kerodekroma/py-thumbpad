import math

# Function to calculate angle in degrees from reference_coord to mouse position
def calculate_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    radians = math.atan2(dy, dx)
    degrees = math.degrees(radians)
    return degrees

def get_direction(angle):
    if angle == 0:
        return None

    if -135 <= angle < -45:
        return 'top'

    if  angle >= 135 or angle < -135:
        return "left"

    if -45 <= angle < 45:
        return "right"

    if  45 <= angle < 135:
        return "bottom"
    
    return None