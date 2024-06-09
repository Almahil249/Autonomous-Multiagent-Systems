"""Maze_Solver controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, GPS, Motor
import math

# Constants
TIME_STEP = 64
MAX_SPEED = 6.28
THRESHOLD_DISTANCE = 0.1
THRESHOLD_ANGLE = 3.15

# Initialize the robot
robot = Robot()

# Get devices
gps = robot.getDevice('gps')
gps.enable(TIME_STEP)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Read path from file
def read_path(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z = map(float, line.strip().split(','))
            points.append((x, y))
    return points

path = read_path('shortest_path.txt')

# Calculate the angle between two points

def calculate_angle(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    return angle

# Calculate the distance between two points

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


# Main loop
current_point = 0

while robot.step(TIME_STEP) != -1:
    x, y, z = gps.getValues()
    target_x, target_y = path[current_point]
    angle = calculate_angle(x, y, target_x, target_y)
    distance = calculate_distance(x, y, target_x, target_y)
    
    if distance < THRESHOLD_DISTANCE:
        current_point += 1
        if current_point == len(path):
            break
        target_x, target_y = path[current_point]
        angle = calculate_angle(x, y, target_x, target_y)
        distance = calculate_distance(x, y, target_x, target_y)
    
    if abs(angle - z) > THRESHOLD_ANGLE:
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(-MAX_SPEED)
    else:
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)
    
    print(f'Current point: {current_point}, x: {x}, y: {y}, angle: {z}, target_x: {target_x}, target_y: {target_y}, angle: {angle}, distance: {distance}')
    
    pass