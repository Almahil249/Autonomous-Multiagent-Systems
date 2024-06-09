#read shortest_path.txt
#and plot the path
import matplotlib.pyplot as plt
import numpy as np

def read_path(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y, z = map(float, line.strip().split(','))
            points.append((x, y))
    return points

path = read_path('shortest_path.txt')

path = np.array(path)
plt.plot(path[:,0], path[:,1])

plt.show()
