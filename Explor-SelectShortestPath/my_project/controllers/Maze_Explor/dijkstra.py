import heapq
import math

def read_map(file_name):
    points = []
    with open(file_name, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            points.append((x, y))
    return points

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def dijkstra(start, points):
    graph = {point: [] for point in points}
    for point in points:
        for neighbor in points:
            if point != neighbor:
                graph[point].append((euclidean_distance(point, neighbor), neighbor))
    
    queue = [(0, start)]
    distances = {point: float('inf') for point in points}
    distances[start] = 0
    previous = {point: None for point in points}
    
    while queue:
        current_distance, current_point = heapq.heappop(queue)
        
        if current_distance > distances[current_point]:
            continue
        
        for neighbor_distance, neighbor in graph[current_point]:
            distance = current_distance + neighbor_distance
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_point
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, previous

def find_shortest_path(start, points, end_x_range, end_y_range):
    distances, previous = dijkstra(start, points)
    
    goal_points = [point for point in points if end_x_range[0] <= point[0] <= end_x_range[1] and end_y_range[0] <= point[1] <= end_y_range[1]]
    if not goal_points:
        return None
    
    goal_point = min(goal_points, key=lambda point: distances[point])
    
    path = []
    while goal_point:
        path.append(goal_point)
        goal_point = previous[goal_point]
    
    path.reverse()
    return path

def save_path(path, file_name):
    with open(file_name, 'w') as file:
        for point in path:
            file.write(f"{point[0]},{point[1]}")

def main():
    start = (-1.9000003736837108, 1.026837301695949)
    end_x_range = (0.9157519785558946, 1.2033550248884672)
    end_y_range = (-1.9153359914579067, -1.7875241920627043)
    
    points = read_map('map.txt')
    path = find_shortest_path(start, points, end_x_range, end_y_range)
    
    if path:
        save_path(path, 'Best_path.txt')
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
