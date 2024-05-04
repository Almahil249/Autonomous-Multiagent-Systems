# BFS 
# We need to go from node A to node C with the shortest path possible
# We have the following graph:
# path cost: (A -> B) = 6 , (A -> D) = 1 , (D -> B) = 2 , (D -> E) = 1 , (B -> C) = 5 , (E -> C) = 5,  (E -> B) = 2

""""

(A)----6----(B) \\
 |        /       \ 
 1      / 2         5 (C)
 |   /            /
(D)----1----(E) /

                        (A)
                   /          \\
                  B             D
             /   |    \       /     \  
            C    E     D     B       E 
                                     |
                                     C
"""

# The BFS algorithm works as follows:
# 1. Start at the initial node
# 2. Add the initial node to the queue
# 3. While the queue is not empty:
#    a. Remove the first node from the queue
#    b. If the node is the goal node, return the path
#    c. Add the neighbors of the node to the queue

# We need to store the state of the nodes and the path to the node
# We can use a queue to store the nodes

from collections import deque

graph = {
    'A': ['B', 'D'],
    'B': ['C'],
    'D': ['B', 'E'],
    'E': ['B', 'C']
}

# BFS algorithm implementation parameters are graph, start node, goal node and it returns 
def bfs(graph, start, goal):
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None

path = bfs(graph, 'A', 'C')

print(f'The BFS algorithm finds the shortest path from node A to node C: {path}')

# The BFS algorithm finds the shortest path from node A to node C: ['A', 'B', 'C'] with a path cost of 11
# The BFS algorithm is not optimal and may not find the shortest path in some cases