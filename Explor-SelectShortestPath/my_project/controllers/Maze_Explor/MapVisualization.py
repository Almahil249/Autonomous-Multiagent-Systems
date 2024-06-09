#read path.txt wich contains the path of the robot
# it is gps coordinates x.y,z
#each line is a point of the path
#each point is separated by a comma like tis -1.9000003736837092, 1.0268373016959478, 0.09854148554694897
# each run of the robot is separated "!!Run" line

import matplotlib.pyplot as plt
import numpy as np
import sys

def read_file(file_name):
    #read the
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return lines

def get_points(lines):
    points = []
    for line in lines:
        if "!!Run" in line:
            points.append([])
        else:
            point = line.split(",")
            points[-1].append([float(point[0]), float(point[1]), float(point[2])])
    return points

def export_map(points):
    file = open("map.txt", "w")
    for run in points:
        for point in run:
            file.write(str(point[0]) + "," + str(point[1]) + "\n")
    file.close()

def plot_points(points):
    for run in points:
        x = []
        y = []
        for point in run:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y)
    #export the plot to a file so it can be used in the report
    plt.savefig("map.png")
    plt.show()


def main(): 
    file_name = file_name = 'path.txt'
    lines = read_file(file_name)
    points = get_points(lines)
    plot_points(points)
    export_map(points)


if __name__ == "__main__":
    main()