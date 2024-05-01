"""Wall_follower controller."""

# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor

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

    S1 = robot.getDevice('Sensor1')
    S2 = robot.getDevice('Sensor2')
    S8 = robot.getDevice('Sensor8')

    S1.enable(timestep)
    S2.enable(timestep)
    S8.enable(timestep)

    prox_sensors = [S1, S2, S8]
    flag = False


    while robot.step(timestep) != -1:
        for i in range(3):
            print("sensor: {} value: {}".format(i, prox_sensors[i].getValue()))

        front_wall = prox_sensors[0].getValue() < 1000
        left_wall = prox_sensors[1].getValue() < 1000

        
        print('Fwall',front_wall)
        print('Lft wall',left_wall)

        left_speed = max_speed
        right_speed = max_speed
        
        
        if not front_wall and not left_wall and not flag:
            print("Searching for some walls")
            left_speed = max_speed
            right_speed= max_speed

        elif left_wall:
            flag = True
            print("turn right")
            left_speed = max_speed/2
            right_speed = -max_speed
       
        elif front_wall:
            flag = True
            print("Drive forward")
            left_speed = max_speed
            right_speed = max_speed
        else:
            print("turn left")
            left_speed = max_speed/5
            right_speed = max_speed

        L1.setVelocity(left_speed)
        L2.setVelocity(left_speed)
        R1.setVelocity(right_speed) 
        R2.setVelocity(right_speed) 




        pass


if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)
