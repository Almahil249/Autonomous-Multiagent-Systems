#read path.txt wich contains the path of the robot
# it is gps coordinates x.y,z
#each line is a point of the path
#each point is separated by a comma like tis -1.9000003736837092, 1.0268373016959478, 0.09854148554694897
# each run of the robot is separated "!!Run" line

import matplotlib.pyplot as plt
import numpy as np
import sys

def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return lines

def get_points(lines):
    points = []
    Time = []
    Itieartion = []
    for line in lines:
        if "!!Run" in line:
            points.append([])
        elif "!T:" in line:
            Time.append(float(line.split(":")[1]))
        elif "!I:" in line:
            Itieartion.append(int(line.split(":")[1]))
        else:
            point = line.split(",")
            points[-1].append([float(point[0]), float(point[1]), float(point[2])])
    return points, Time, Itieartion

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


def plot_shortest_path():
    with open('shortest_path.txt') as f:
        lines = f.readlines()
    x = []
    y = []
    for line in lines:
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    plt.plot(x, y, 'ro')
    plt.show()


def plot_points_and_shortest_path(points):
    for run in points:
        x = []
        y = []
        for point in run:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x, y)
    with open('shortest_path.txt') as f:
        lines = f.readlines()
    x = []
    y = []
    for line in lines:
        x.append(float(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    plt.plot(x, y, 'ro')
    plt.savefig("map_and_shortest_path.png")
    plt.show()





def main(): 
    file_name = file_name = 'path.txt'
    lines = read_file(file_name)
    points, Time, Itieartion  = get_points(lines)
    plot_points_and_shortest_path(points)
    plot_points(points)
    plot_shortest_path()
    export_map(points)
    ifile = open("ExplorSummary.txt", "w")
    for i in range(len(Itieartion)):
        ifile.write(f"Run {i+1}: Time: {Time[i]} Iterations: {Itieartion[i]}\n")
    ifile.close()



if __name__ == "__main__":
    main()