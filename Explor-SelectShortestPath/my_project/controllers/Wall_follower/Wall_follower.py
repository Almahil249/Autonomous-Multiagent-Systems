"""Wall_follower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
# Import necessary libraries
from controller import Robot, Motor, DistanceSensor, GPS

# Constants
TIME_STEP = 64
MAX_SPEED = 6.28

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
for sensor in ps:
    sensor.enable(TIME_STEP)

# Open file to record path
file = open("path.txt", "w")

def write_position():
    pos = gps.getValues()
    file.write(f"{pos[0]}, {pos[1]}, {pos[2]}\n")

# Main loop
while robot.step(TIME_STEP) != -1:
    # Read sensors
    ps_values = [sensor.getValue() for sensor in ps]
    
    # Simple obstacle avoidance
    right_obstacle = ps_values[0] > 80.0 or ps_values[1] > 80.0 or ps_values[2] > 80.0
    left_obstacle = ps_values[5] > 80.0 or ps_values[6] > 80.0 or ps_values[7] > 80.0
    
    # Write current position to file
    write_position()
    
    # Decision making based on sensor values
    if left_obstacle:
        # Turn right
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(-MAX_SPEED)
    elif right_obstacle:
        # Turn left
        left_motor.setVelocity(-MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)
    else:
        # Move forward
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)

# Close the file
file.close()




"""

from controller import Robot

def run_robot(robot):
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28

    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')

    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    prox_sensors = []
    for i in range(8):
        sensor_name = 'ps' + str(i)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[i].enable(timestep)

    while robot.step(timestep) != -1:
        for i in range(8):
            print("sensor: {} value: {}".format(i, prox_sensors[i].getValue()))

        left_wall = prox_sensors[5].getValue() > 80
        front_wall = prox_sensors[7].getValue() > 80 

        left_speed = max_speed
        right_speed = max_speed

        if front_wall:
            print("turn right")
            left_speed = max_speed
            right_speed = -max_speed
        else:
            if left_wall:
                print("Drive forward")
                left_speed = max_speed
                right_speed = max_speed
            else:
                print("turn left")
                left_speed = max_speed/4
                right_speed = max_speed

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed) 


        pass


# Enter here exit cleanup code.
if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)
"""