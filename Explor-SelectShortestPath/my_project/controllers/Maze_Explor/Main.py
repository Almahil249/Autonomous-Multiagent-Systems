import heapq
import matplotlib.pyplot as plt
import numpy as np

# Constants
paths_file_name = 'path.txt'
summary_file_name = 'ExplorSummary.txt'
shortestPath_file_name = 'shortest_path.txt'

# Function to parse the dataset to extract the runs summary
def parse_dataset(filename):
    runs = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Run'):
                parts = line.split()
                run_id = int(parts[1][:-1])
                time = float(parts[3])
                iterations = int(parts[5])
                distance = float(parts[7])
                runs.append((run_id, distance, time, iterations))
    f.close()
    return runs    

# Dijkstra's algorithm
def find_best_run(runs, weight_distance=1.8, weight_time=0.85, weight_iterations=0.80):
    pq = []
    for run in runs:
        _, distance, time, iterations = run
        cost = (weight_distance * distance) + (weight_time * time) + (weight_iterations * iterations)
        heapq.heappush(pq, (cost, run))    
    best_run = heapq.heappop(pq)
    return best_run

def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return lines

def get_best_run_details(id):
    lines = read_file(paths_file_name)
    points = []
    currnt_run = 0
    for line in lines:
        if "!!Run" in line:
            currnt_run += 1
        elif "!T:" in line:
            if currnt_run == id:
                break
        else:
            if currnt_run == id:
                points.append(line)
    #save the best run details to a file
    file = open(shortestPath_file_name, "w")
    for run in points:
        for point in run:
            file.write(point)
    file.close()
    import shutil
    shutil.copy(shortestPath_file_name, "C:\\Users\\aalma\\Desktop\\AMS\\Explor-SelectShortestPath\\my_project\\controllers\\Maze_Solver")


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
    plt.title("Map")
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
    f.close()
    plt.plot(x, y, 'ko')
    plt.title("Shortest Path")
    plt.show()


def plot_points_and_shortest_path(points, best_run):
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
    f.close()
    plt.plot(x, y, 'ko')
    plt.title("Map and Shortest Path")
    plt.xlabel(f"The best run is Run {best_run[1][0]} with Time {best_run[1][2]} and Distance {best_run[1][1]}", fontsize=12)
    plt.savefig("map_and_shortest_path.png")
    plt.show()



# calculate path total distance for each run
def calculate_distance(points):
    distance = []
    for run in points:
        dist = 0
        for i in range(len(run) - 1):
            dist += np.sqrt((run[i][0] - run[i+1][0])**2 + (run[i][1] - run[i+1][1])**2)
        distance.append(dist)
    return distance





def main(): 
    lines = read_file(paths_file_name)
    points, Time, Itieartion  = get_points(lines)
    distance = calculate_distance(points)
    export_map(points)
    SummaryFile = open(summary_file_name, "w")
    for i in range(len(Itieartion)):
        SummaryFile.write(f"Run {i+1}: Time: {Time[i]} Iterations: {Itieartion[i]} Distance: {distance[i]}\n")
    SummaryFile.close()


    runs = parse_dataset(summary_file_name)
    best_run = find_best_run(runs)
    get_best_run_details(best_run[1][0])
    plot_points(points)
    plot_shortest_path()
    plot_points_and_shortest_path(points, best_run)


if __name__ == "__main__":
    main()



