#DFS algorithm
# We need to go from node A to node C with the shortest path possible
# We have the following graph:
# path cost: (A -> B) = 6 , (A -> D) = 1 , (D -> B) = 2 , (D -> E) = 1 , (B -> C) = 5 , (E -> C) = 5,  (E -> B) = 2

""""

(A)----6----(B) \\
 |        /  |    \ 
 1      2    2      5 (C)
 |   /       |    /
(D)----1----(E) /

                        (A)
                   /          \\
                  B             D
             /   |    \       /     \  
            C    E     D     B       E 
                                     |
                                     C
                        (A)
                   /          \\
                  D             B
              /     \        /  |   \  
             E       B      c   E    D 
             |
             C


"""

# We can use the Depth First Search (DFS) algorithm to find the shortest path from node A to node C
# The DFS algorithm works as follows:
# 1. Start at the initial node
# 2. Add the initial node to the stack
# 3. While the stack is not empty:
#    a. Remove the last node from the stack
#    b. If the node is the goal node, return the path
#    c. Add the neighbors of the node to the stack

# We need to store the state of the nodes and the path to the node
# We can use a stack to store the nodes

graph = {
    'A': ['B', 'D'],
    'B': ['C'],
    'D': ['B', 'E'],
    'E': ['B', 'C']
}


def dfs(graph, start, goal):
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            stack.append(new_path)
    return None


path = dfs(graph, 'A', 'C')

print(f'The DFS algorithm finds the shortest path from node A to node C: {path}')

