"""Maze_Explor controller."""
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
gps = robot.getDevice('gps')
ps = []
for i in range(8):
    ps.append(robot.getDevice(f'ps{i}'))

# Enable devices
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
gps.enable(TIME_STEP)
grnd = robot.getDevice('Ground')
grnd.enable(TIME_STEP)
for sensor in ps:
    sensor.enable(TIME_STEP)

file = open("path.txt", "a")
file.write("!!Run\n")

def write_position(status, left_random, right_random):
    pos = gps.getValues()
    file.write(f"{pos[0]}, {pos[1]}, {pos[2]}, {status}, {left_random}, {right_random}\n")

iteration = 0
start_time = time.time()
while robot.step(TIME_STEP) != -1:
    iteration += 1
    if flag == False:
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)
        print("! MAZE !")
        if grnd.getValue() > 190 and grnd.getValue() < 210:
            flag = True
            print("ON THE Maze")
    else:
        left_random = random.uniform(0.05, 0.95)
        right_random = random.uniform(0.05, 0.95)
        # Read sensors
        ps_values = [sensor.getValue() for sensor in ps]
        #print(grnd.getValue())
        #242-294 start red   700-920 endd blue
        is_start = grnd.getValue() >= 242 and grnd.getValue() <= 294
        is_end = grnd.getValue() >= 700 and grnd.getValue() <= 920
        # Simple obstacle avoidance
        right_obstacle = ps_values[0] > 80.0 or ps_values[1] > 80.0 or ps_values[2] > 80.0
        left_obstacle = ps_values[5] > 80.0 or ps_values[6] > 80.0 or ps_values[7] > 80.0
        
        # stochastic obstacle avoidance
        if is_start: #turn 360
            write_position('On_start', 1, 1)
            left_motor.setVelocity(MAX_SPEED)
            right_motor.setVelocity(-MAX_SPEED)
            print(grnd.getValue())
            print("Start")
            continue
        if is_end: #stop
            write_position("Target", 1, 1)
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)
            print(grnd.getValue())
            print("End")
            break
        if left_obstacle:
            # Turn right
            write_position('left_obstacle', left_random, right_random)
            left_motor.setVelocity(MAX_SPEED*left_random)
            right_motor.setVelocity(-MAX_SPEED*right_random)
        elif right_obstacle:
            # Turn left
            write_position('right_obstacle', left_random, right_random)
            left_motor.setVelocity(-MAX_SPEED*left_random)
            right_motor.setVelocity(MAX_SPEED*right_random)
        else:
            # Move forward
            write_position('Move_forward', 1, 1)
            left_motor.setVelocity(MAX_SPEED)
            right_motor.setVelocity(MAX_SPEED)
end_time = time.time()
print("Time taken: ", end_time - start_time)
print("Number of iterations: ", iteration)
file.write(f"!T: {end_time - start_time}\n")
file.write(f"!I: {iteration}\n")
file.close()

# call and run the Main.py 
import Main as M

M.main()

