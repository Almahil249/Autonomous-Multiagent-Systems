"""Wall_follower controller."""

# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor
import random

def run_robot(robot):
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28

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

    SL = robot.getDevice('SensorL')
    SR = robot.getDevice('SensorR')

    SL.enable(timestep)
    SR.enable(timestep)
    
    S2 = robot.getDevice('Sensor2')
    S8 = robot.getDevice('Sensor8')

    S2.enable(timestep)
    S8.enable(timestep)


    prox_sensors = [SL, SR, S2, S8]
    flag = False
    right_speed = max_speed
    left_speed = max_speed
    
    flag = True

    while robot.step(timestep) != -1:
        L_val = prox_sensors[0].getValue()
        R_val = prox_sensors[1].getValue()
        
        right_speed = max_speed
        left_speed = max_speed
        
        L_line = L_val > 900
        R_line = R_val > 900
        
        
        if flag:
            
            if L_line or R_line:
                flag = False
            psRightValue = S2.getValue()
            psLeftValue = S8.getValue()
        
            rightObstacle= psRightValue<900
            leftObstacle= psLeftValue<900

            randL = random.uniform(0.01, 0.99)
            randR = random.uniform(0.01, 0.99)

            left_speed =  randL * max_speed
            right_speed = randR * max_speed
            
            
            if rightObstacle and leftObstacle:
                print("BOTH Obstacle")
                left_speed = -max_speed
                right_speed = -max_speed
            
            elif rightObstacle:
                print("Right Obstacle")
                left_speed = max_speed
                right_speed =  -0.5 * max_speed
        
            elif leftObstacle:
                print("Left Obstacle")
                left_speed =  -0.5 * max_speed
                right_speed = max_speed
             
       
        else:
            print("sensor: Left value: {}".format(L_val))
            print("sensor: Right value: {}".format(R_val))
            print("________________________________________________")
            
            if L_val > R_val and L_line:
                left_speed = -max_speed 
                print("Drive Left")
                print("________________________________________________")
    
            elif R_val > L_val and R_line:
                right_speed = -max_speed 
                print("Drive Right")
                print("________________________________________________")
            else:
                print("Drive FW")
                print("________________________________________________")
    


        
    
    
        
        


        L1.setVelocity(left_speed)
        L2.setVelocity(left_speed)
        R1.setVelocity(right_speed) 
        R2.setVelocity(right_speed) 




        pass


if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)
