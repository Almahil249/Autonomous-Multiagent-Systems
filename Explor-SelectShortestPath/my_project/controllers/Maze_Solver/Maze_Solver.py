from controller import Robot, Motor, GPS

TIME_STEP = 64
MAX_SPEED = 6.28

robot = Robot()
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
gps = robot.getDevice('gps')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
gps.enable(TIME_STEP)

try:
    path_file = open("path.txt", "r")
    path_lines = path_file.readlines()
    path_file.close()
except FileNotFoundError:
    print("Path file not found. Make sure 'path.txt' exists.")
    exit()

path_index = 0

def get_next_path_position():
    global path_index
    if path_index < len(path_lines):
        path_line = path_lines[path_index].strip().split(',')
        path_index += 1
        return float(path_line[0]), float(path_line[1])
    else:
        return None, None

while robot.step(TIME_STEP) != -1:
    current_x, current_y, _ = gps.getValues()
    next_x, next_y = get_next_path_position()

    if next_x is not None and next_y is not None:
        dx = next_x - current_x
        dy = next_y - current_y

        if abs(dx) > abs(dy):
            if dx > 0:
                left_motor.setVelocity(MAX_SPEED)
                right_motor.setVelocity(MAX_SPEED * 0.5)
            else:
                left_motor.setVelocity(MAX_SPEED * 0.5)
                right_motor.setVelocity(MAX_SPEED)
        else:
            if dy > 0:
                left_motor.setVelocity(MAX_SPEED)
                right_motor.setVelocity(MAX_SPEED)
            else:
                left_motor.setVelocity(-MAX_SPEED)
                right_motor.setVelocity(-MAX_SPEED)


        if abs(dx) < 0.1 and abs(dy) < 0.1:
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        print("Reached the end of the path.")
        break


"""# Follow Path Controller

from controller import Robot, GPS, Motor, Compass
import math

# Constants
TIME_STEP = 64
MAX_SPEED = 6.28
THRESHOLD_DISTANCE = 0.07
THRESHOLD_ANGLE = 0.3

# Initialize the robot
robot = Robot()

# Get devices
gps = robot.getDevice('gps')
gps.enable(TIME_STEP)

compass = robot.getDevice('compass')
compass.enable(TIME_STEP)

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
            if line.strip() and not line.startswith('!!') and not line.startswith('!'):
                parts = line.strip().split(', ')
                if len(parts) >= 3:
                    x, y = map(float, parts[:2])
                    points.append((x, y))
    return points

path = read_path('path1.txt')

# Helper functions
def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 )

def get_bearing(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.atan2(dy, dx)

def get_current_bearing():
    compass_values = compass.getValues()
    rad = -math.atan2(compass_values[0], compass_values[2])
    return rad

def normalize_angle(angle):
    while angle > math.pi:
        angle -= 2.0 * math.pi
    while angle < -math.pi:
        angle += 2.0 * math.pi
    return angle

# Main loop
current_index = 0
while robot.step(TIME_STEP) != -1:
    print("\t**********************")
    current_position = gps.getValues()
    
    if current_index >= len(path):
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
        break
    
    target_position = path[current_index]
    
    current_position
    print("current_position: " , current_position)
    print("target_position: " , target_position)
    
    
    distance_to_target = get_distance(current_position, target_position)
    print("distance_to_target: " , distance_to_target)

    if distance_to_target < THRESHOLD_DISTANCE:
        current_index += 1
        print("CCCCCCCCCCCCCCCCCCCCCCCC")
        continue
    print("\t#####################")
    current_bearing = get_current_bearing()
    print("current_bearing: " , current_bearing)

    
    target_bearing = get_bearing(current_position, target_position)
    angle_to_target = (target_bearing - current_bearing)
    print("target_bearing: " , target_bearing)
    print("angle_to_target: " , angle_to_target)
    print("\n_______________________________________\n")

    if abs(angle_to_target) > THRESHOLD_ANGLE:
        if angle_to_target > 0:
            left_motor.setVelocity(MAX_SPEED )
            right_motor.setVelocity(-MAX_SPEED)
        else:
            left_motor.setVelocity(-MAX_SPEED)
            right_motor.setVelocity(MAX_SPEED)
    else:
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)
"""