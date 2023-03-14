import copy
import math
import matplotlib.pyplot as plt

# function to draw a scatterplot of centroids and clusters
# you can also put pieces of this function directly into the relevant spots in the code
# parameters: centroids (list), clusters (list)
def plot_cluster(centroids, clusters):
    colors = ["black", "blue", "green", "orange"]
    plt.xlabel("x-coordinates") # label x-axis
    plt.ylabel("y-coordinates") # label y-axis

    # collect all x-values, y-values for drawing with matplotlib
    # uses a list comprehension, could also use a regular for loop
    x = [point[0] for point in centroids] # collect x-values in a list
    y = [point[1] for point in centroids] # collect y-values in a list

    plt.scatter(x, y, color="red", s=100) # draw scatterplot to the canvas

    # collect all x-values, y-values for drawing with matplotlib
    for i, cluster in enumerate(clusters):
        x = [point[0] for point in cluster] # collect x-values in a list
        y = [point[1] for point in cluster] # collect y-values in a list

        plt.scatter(x, y, color=colors[i]) # draw scatterplot to the canvas

    # render canvas to the screen
    plt.show()

################################################################################

cluster_changes = 0
clusters = []
distances = []
points = []
prev_cluster_size = []
X = 0 # used for convenient indexing of x-coordinates
Y = 1 # used for convenient indexing of y-coordinates

################################################################################

# open points.txt for reading points from file
f = open("kmeans.txt", "r")

iterations = int(f.readline()) # read number of clustering iterations from file
num_points = int(f.readline()) # read number of points from file
num_clusters = int(f.readline()) # read number of clusters from file
cluster_indexes = [] # read cluster indexes from file

# store a list of cluster indexes, will use this later to copy the initial centroids
for i in range(num_clusters):
    cluster_indexes.append(int(f.readline()))

# create a list of k initially empty clusters (lists)
# uses a list comprehension, could also use a regular for loop
clusters = [[] for i in range(num_clusters)]

# create a list of k previous cluster sizes, each initially 0 (empty)
# uses a list comprehension, could also use a regular for loop
prev_cluster_size = [0 for i in range(num_clusters)]

# read and parse points from file into a list
for line in range(num_points):
    point = f.readline().strip().split(',') # remove newlines, split on commas
    x = int(point[0]) # parse x-coordinate
    y = int(point[1]) # parse y-coordinate
    points.append([x, y]) # add point to list

# create a list of centroids using
centroids = []
for index in cluster_indexes:
    # depending on your implementation you may need to copy the initial centroids
    # otherwise they might be overwritten when we compute the new centroids
    centroids.append(copy.copy(points[index]))

################################################################################

print(f"Initial COVID-19 Patients: {centroids}\n")

for r in range(iterations):
    for point in points:
        # calculate the distance between the current point and each of the 4 centroids
        for i in range(len(centroids)):
            distance = math.sqrt((centroids[i][X] - point[0]) ** 2 + (centroids[i][Y] - point[1]) ** 2)
            distances.append(distance)

        # assign each point to the cluster to which it is closest
        for i in range(len(distances)):
            if distances[i] == min(distances):
                clusters[i].append(point)

        # clear distances list before next iteration
        distances.clear()

    # check if any points have changed clusters
    for i in range(len(clusters)):
        if len(clusters[i]) != prev_cluster_size[i]:
            cluster_changes += 1
            break

    # calculate the resulting centroid for each cluster using the mean
    for i in range(len(clusters)):
        total_x = 0
        total_y = 0

        # sum the x and y coordinates of each point in the current cluster
        for point in clusters[i]:
            total_x += point[X]
            total_y += point[Y]

        # update centroid with the resulting cluster's mean x and y values
        centroids[i][X] = total_x / len(clusters[i])
        centroids[i][Y] = total_y / len(clusters[i])

        # store current cluster size for comparison in next iteration
        prev_cluster_size[i] = len(clusters[i])

    # draw a scatterplot of the initial clustering
    if r == 0:
        plot_cluster(centroids, clusters)

    # empty the cluster except on final iteration
    if r < iterations - 1:
        for cluster in clusters:
            cluster.clear()

# output number of iterations until clusters are stable
print(f"Iterations to achieve stability: {cluster_changes}\n")

print("Final Centroids:")
for centroid in centroids:
    print(f"{centroid}")

print()

# output the centroid, the number of points, and a list of points for each cluster
for i in range(len(clusters)):
    print(f"Number of patients in Cluster {i}: {len(clusters[i])}")
    print(f"{clusters[i]}\n")

# draw a scatterplot of the final clustering
plot_cluster(centroids, clusters)