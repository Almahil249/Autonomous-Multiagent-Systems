from controller import Robot, DistanceSensor,Motor
import time

TIME_STEP = 64
SPEED = 6.8
# create the Robot instance.
robot = Robot()
# initialize devices
# Sensor1 @ 0 degree, Sensor2 @ 45 degree, Sensor3 @ 90 degree, Sensor4 @ 135 degree, Sensor5 @ 180 degree, Sensor6 @ 225 degree, Sensor7 @ 270 degree, Sensor8 @ 315 degree

LS.enable(TIME_STEP)
RS.enable(TIME_STEP)

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


# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    LS_val = LS.getValue()
    RS_val = RS.getValue()
    print("L_Sensor:",LS_val)
    print("R_Sensor:",RS_val)
    # detect obstacles

    right_obstacle = RS_val < 1000.0
    left_obstacle = LS_val < 1000.0

    leftSpeed  = 0.75 * SPEED
    rightSpeed = 0.75 * SPEED


    if right_obstacle:
        # turn left
        leftSpeed  = -1.2 * SPEED
        rightSpeed = .75 * SPEED
        
    elif left_obstacle:
        # turn right
        leftSpeed  = .75 * SPEED
        rightSpeed = -1.2 * SPEED

       

    L1.setVelocity(leftSpeed)
    L2.setVelocity(leftSpeed)
    R1.setVelocity(rightSpeed)
    R2.setVelocity(rightSpeed)

