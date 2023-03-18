import copy
import math

# import matplotlib.pyplot as plt


def parse_patient_info(lines, index):
    parsedLocation = lines[index].strip().split(",")
    return [int(parsedLocation[0]), int(parsedLocation[1])]


def has_size_change(list1, list2):
    if len(list1) is not len(list2):
        return True
    for i in range(len(list1)):
        if list1[i] is not list2[i]:
            return True
    return False


"""
def plotClusters(first_time):
    # area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii
    color_index = 0
    for key, value in cluster_map.items():
        x = [i[0] for i in value]
        y = [i[1] for i in value]
        color = colors[color_index]
        plt.scatter(x, y, s=[15 for i in range(len(x))], c=color)
        color_index = color_index + 1
    for i in initial_patients_list:
        plt.scatter(i[0], i[1], s=[40], c="#ff0000")
    plt.xlabel("x-coordinates")
    plt.ylabel("y-coordinates")
    if first_time:
        plt.title("Initial clustering after 1 iteration")
    else:
        plt.title("Final clustering after k-means reaches convergence")
    plt.show()
"""

# Read and parse all fields from input file and initialize variables
lines = []
with open('points2.txt') as f:
    lines = f.readlines()

max_num_of_iter = int(lines[0])
num_of_patients = int(lines[1])
total_num_of_clusters = int(lines[2])

# Assign the starting index
starting_index = 3 + total_num_of_clusters

# Initialize patient lists
initial_patients_list = list()
patients_list = list()
initial_patients_indices = [int(lines[i]) for i in range(3, starting_index)]

# Matplotlib Colors
colors = ["#000000", "#0000FF", "#88c999", "#FFA500"]

# Append data to initial patient list and create map to keep track of clusters
cluster_map = dict()
for i in range(len(initial_patients_indices)):
    initial_patients_list.append(parse_patient_info(
        lines, initial_patients_indices[i] + starting_index))
    cluster_map[i] = list()
original_initial_patients_indices = copy.deepcopy(initial_patients_list)

# Append data to patient list
for i in range(starting_index, len(lines)):
    patients_list.append(parse_patient_info(lines, i))

iteration_count = 0
current_cluster_size = [0, 0, 0, 0]

# For number of iterations in input file
for i in range(max_num_of_iter):
    # For each patient in the input file
    for patient in patients_list:
        closest_cluster = -1
        shortest_distance = float("inf")

        # Calculate distance between current patient and all k centroids
        for j in range(total_num_of_clusters):
            initial_patient = initial_patients_list[j]
            distance = math.sqrt(
                math.pow(patient[0] - initial_patient[0], 2) + math.pow(patient[1] - initial_patient[1], 2))
            if distance < shortest_distance:
                closest_cluster = j
                shortest_distance = distance

        # Assign patient to the cluster with the nearest centroid
        cluster_map[closest_cluster].append(patient)

    # Check if any patients have changed clusters
    if has_size_change(current_cluster_size, [len(value) for key, value in cluster_map.items()]):
        # Update the iteration count
        iteration_count = iteration_count + 1

    # Calculate cluster mean x/y and update centroid for each cluster
    for j in range(total_num_of_clusters):
        x_values = [x[0] for x in cluster_map[j]]
        x = sum(x_values) / len(x_values)
        y_values = [y[1] for y in cluster_map[j]]
        y = sum(y_values) / len(y_values)
        initial_patients_list[j] = [x, y]

    # Save current cluster sizes (for comparison in next iteration)
    current_cluster_size = [len(value) for key, value in cluster_map.items()]

    # if i == 1:
    #    plotClusters(True)

    # Empty clusters for re-clustering except on final iteration
    if i is not max_num_of_iter - 1:
        for j in range(len(initial_patients_indices)):
            cluster_map[j] = list()

# Final cluster map
# plotClusters(False)

# Output results in specified format
print(f"Initial COVID-19 Patients: {original_initial_patients_indices}\n")
print(f"Iterations to achieve stability: {iteration_count}\n")
print("Final Centroids:")
for c in initial_patients_list:
    print(c)
for j in range(total_num_of_clusters):
    cluster_patients = cluster_map[j]
    print(f"\nNumber of patients in Cluster {j}: {len(cluster_patients)}")
    print(cluster_patients)
