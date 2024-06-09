# read map.txt and plot the points
import matplotlib.pyplot as plt
file = open("map.txt", "r")
lines = file.readlines()
file.close()

#rempve and duplicate lines
lines = list(dict.fromkeys(lines))
X = []  
Y = []
#plot the points as a points
for line in lines:
    x, y = line.split(",")
    X.append(float(x))
    Y.append(float(y))
plt.plot(X, Y, 'ro')
plt.show()

