def parse_path(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            if "!!Run" in line:
                continue
            x, y, z = map(float, line.strip().split(","))
            points.append((x, y, z))
    return points

points = parse_path('path.txt')

import math

def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
from queue import PriorityQueue

def a_star(start, goal, points):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {point: float('inf') for point in points}
    g_score[start] = 0
    f_score = {point: float('inf') for point in points}
    f_score[start] = heuristic(start, goal)
    i = 0
    while not open_set.empty():
        print(i)
        i += 1
        _, current = open_set.get()
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in get_neighbors(current, points):
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))
    
    return []

def get_neighbors(node, points):
    threshold = 0.00005  
    neighbors = []
    for point in points:
        if heuristic(node, point) < threshold and node != point:
            neighbors.append(point)
    return neighbors

start = points[0]
goal = points[-1]
shortest_path = a_star(start, goal, points)

def save_shortest_path(path, file_path):
    with open(file_path, 'w') as file:
        for point in path:
            file.write(f"{point[0]}, {point[1]}, {point[2]}\n")

save_shortest_path(shortest_path, 'shortest_path.txt')
