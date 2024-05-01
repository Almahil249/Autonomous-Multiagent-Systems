from controller import Robot, DistanceSensor,Motor
import time

TIME_STEP = 64
SPEED = 6.8
# create the Robot instance.
robot = Robot()
# initialize devices
# Sensor1 @ 0 degree, Sensor2 @ 45 degree, Sensor3 @ 90 degree, Sensor4 @ 135 degree, Sensor5 @ 180 degree, Sensor6 @ 225 degree, Sensor7 @ 270 degree, Sensor8 @ 315 degree
S1 = robot.getDevice('Sensor1')
S2 = robot.getDevice('Sensor2')
S3 = robot.getDevice('Sensor3')
S4 = robot.getDevice('Sensor4')
S5 = robot.getDevice('Sensor5')
S6 = robot.getDevice('Sensor6')
S7 = robot.getDevice('Sensor7')
S8 = robot.getDevice('Sensor8')

S1.enable(TIME_STEP)
S2.enable(TIME_STEP)
S3.enable(TIME_STEP)
S4.enable(TIME_STEP)
S5.enable(TIME_STEP)
S6.enable(TIME_STEP)
S7.enable(TIME_STEP)
S8.enable(TIME_STEP)

# initialize motors
L1  = robot.getDevice( 'Left1' )
R1 = robot.getDevice( 'Right1' )
L2 = robot.getDevice( 'Left2' )
R2 = robot.getDevice( 'Right2' )

L1.setPosition(float('inf'))
L2.setPosition(float('inf'))
R1.setPosition(float('inf'))
R2.setPosition(float('inf'))

L1.setVelocity(0.0)
L2.setVelocity(0.0)
R1.setVelocity(0.0)
R2.setVelocity(0.0)

# Main loop:
# follow the wall algorithm to get out of the maze
while robot.step(TIME_STEP) != -1:
    # read sensors
    S1_value = S1.getValue()
    S2_value = S2.getValue()
    S3_value = S3.getValue()
    S4_value = S4.getValue()
    S5_value = S5.getValue()
    S6_value = S6.getValue()
    S7_value = S7.getValue()
    S8_value = S8.getValue()
    
    # if the robot is in a corner, turn right
    if S1_value > 800 and S2_value > 800 and S3_value > 800 and S4_value > 800 and S5_value > 800 and S6_value > 800 and S7_value > 800 and S8_value > 800:
        L1.setVelocity(SPEED)
        L2.setVelocity(SPEED)
        R1.setVelocity(-SPEED)
        R2.setVelocity(-SPEED)
        time.sleep(0.5)
    # if the robot is close to the wall, turn left
    elif S1_value < 800 and S2_value < 800 and S3_value < 800 and S4_value < 800 and S5_value < 800 and S6_value < 800 and S7_value < 800 and S8_value < 800:
        L1.setVelocity(-SPEED)
        L2.setVelocity(-SPEED)
        R1.setVelocity(SPEED)
        R2.setVelocity(SPEED)
    # if the robot is far from the wall, move forward
    else:
        L1.setVelocity(SPEED)
        L2.setVelocity(SPEED)
        R1.setVelocity(SPEED)
        R2.setVelocity(SPEED)
    pass