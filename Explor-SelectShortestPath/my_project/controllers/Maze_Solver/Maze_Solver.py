"""Maze_Solver controller."""
from controller import Robot
import random
import time
# Constants
TIME_STEP = 64
MAX_SPEED = 6.28
flag = False

# Initialize the robot and its devices
robot = Robot()

# Get devices
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
ps = []
for i in range(8):
    ps.append(robot.getDevice(f'ps{i}'))

# Enable devices
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
grnd = robot.getDevice('Ground')
grnd.enable(TIME_STEP)
for sensor in ps:
    sensor.enable(TIME_STEP)


while True:
    try:
        path_file = open("shortest_path.txt", "r")
        break
    except:
        time.sleep(1)
path_lines = path_file.readlines()
path_file.close()

# each line in the file is like 1.213508479349374, -0.5998973881551225, 0.09854416354148647, left_obstacle, 0.6417236943390522, 0.556904176979193
#ignore the first 3 values and save the rest in a list (state ,  left_random, right_random)  left_random, right_random are float values
path = []
for line in path_lines:
    parts = line.strip().split(', ')
    if len(parts) >= 3:
        state = parts[3]
        left_random = float(parts[4])
        right_random = float(parts[5])
        path.append((state, left_random, right_random))

path_index = 0

while robot.step(TIME_STEP) != -1:
    if flag == False:
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)
        print("! MAZE !")
        if grnd.getValue() > 190 and grnd.getValue() < 210:
            flag = True
            print("ON THE Maze")
    else:
        state, left_random, right_random = path[path_index]
        path_index += 1
        
        # Read sensors
        ps_values = [sensor.getValue() for sensor in ps]
        is_start = grnd.getValue() >= 242 and grnd.getValue() <= 294
        is_end = grnd.getValue() >= 700 and grnd.getValue() <= 920
        
        # stochastic obstacle avoidance
        if is_start: #turn 360
            left_motor.setVelocity(MAX_SPEED)
            right_motor.setVelocity(-MAX_SPEED)
            print(grnd.getValue())
            print("Start")
            continue
        if is_end: #stop
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)
            print(grnd.getValue())
            print("End")
            break
        if state == 'left_obstacle' :
            # Turn right
            left_motor.setVelocity(MAX_SPEED*left_random)
            right_motor.setVelocity(-MAX_SPEED*right_random)
        elif state == 'right_obstacle':
            # Turn left
            left_motor.setVelocity(-MAX_SPEED*left_random)
            right_motor.setVelocity(MAX_SPEED*right_random)
        else:
            # Move forward
            left_motor.setVelocity(MAX_SPEED)
            right_motor.setVelocity(MAX_SPEED)
