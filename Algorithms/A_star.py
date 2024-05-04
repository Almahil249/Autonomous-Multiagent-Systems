# A* algorithm implementation

# We need to go from node A to node C with the shortest path possible
# We have the following graph:
# path cost: (A -> B) = 6 , (A -> D) = 1 , (D -> B) = 2 , (D -> E) = 1 , (B -> C) = 5 , (E -> C) = 5,  (E -> B) = 2
# heuristic cost: (A) = 2.5 , (B) = 1.5 , (C) = 0 , (D) = 2.5 , (E) = 1.5

""""

(A)----6----(B) \\
 |        /       \ 
 1      / 2         5 (C)
 |   /            /
(D)----1----(E) /

"""

# The A* algorithm is a pathfinding algorithm that uses the path cost and the heuristic cost to find the shortest path
# The path cost is the cost to go from one node to another
# The heuristic cost is the estimated cost to go from a node to the goal node
# The total cost is the sum of the path cost and the heuristic cost
# we need to store the state of the nodes, the path cost, the heuristic cost and the total cost and ppr previous prefared node

# The algorithm works as follows:
# 1. Start at the initial node
# 2. Calculate the total cost for each neighbor node
# 3. Add the neighbor nodes to the open list
# 4. Select the node with the lowest total cost from the open list
# 5. Move to the selected node
# 6. Repeat steps 2 to 5 until the goal node is reached
# 7. Return the path

# The algorithm uses a priority queue to store the nodes with the lowest total cost

import heapq

graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'C': 5},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5}
}

heuristic_cost = {
    'A': 2.5,
    'B': 1.5,
    'C': 0,
    'D': 2.5,
    'E': 1.5
}
#a_star algorithm implementation parameters are graph, start node, goal node, heuristic cost
def a_star(graph, start, goal, heuristic_cost):
    open_list = []
    closed_list = []
    path_cost = {}
    heuristic = {}
    total_cost = {}
    previous = {}
    heapq.heappush(open_list, (0, start))
    path_cost[start] = 0
    heuristic[start] = heuristic_cost[start]
    total_cost[start] = path_cost[start] + heuristic[start]
    previous[start] = None
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            path.reverse()
            return path, path_cost[goal], heuristic[goal]
        closed_list.append(current_node)
        for neighbor, cost in graph[current_node].items():
            if neighbor in closed_list:
                continue
            new_cost = path_cost[current_node] + cost
            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost
                heuristic[neighbor] = heuristic_cost[neighbor]
                total_cost[neighbor] = path_cost[neighbor] + heuristic[neighbor]
                heapq.heappush(open_list, (total_cost[neighbor], neighbor))
                previous[neighbor] = current_node
    return None

path, path_cost, heuristic_cost = a_star(graph, 'A', 'C', heuristic_cost)
print(f'The shortest path from node A to node C is {path} with a cost of {path_cost}')
print(f'The path cost is {path_cost} and the heuristic cost is {heuristic_cost}')
print(f'The total cost is {path_cost + heuristic_cost}')
print(f'The path is {path}')

# Output:
# The shortest path from node A to node C is ['A', 'D', 'E', 'C'] with a cost of 7
# The shortest path from node A to node C is A -> D -> E -> C with a cost of 7
# The path cost is 7 and the heuristic cost is 0
# The total cost is 7 + 0 = 7
# The path is ['B', 'C']
