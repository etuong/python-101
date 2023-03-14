from matplotlib import pyplot as plt

from Point import Point


# Function to plot the data points
def plot_points(points: Point):
    x_coordinates = [pt.x for pt in points]
    y_coordinates = [pt.y for pt in points]
    plt.plot(x_coordinates, y_coordinates, 'ro')
    plt.show()


# Function to plot the colinear line
def plot_colinear(pointA: Point, pointB: Point):
    plt.plot([pointA.x, pointB.x], [pointA.y, pointB.y], 'b')


if __name__ == '__main__':
    # Read and parse all fields from input file and initialize variables
    lines = []
    with open('points4.txt') as f:
        lines = f.readlines()

    # Initialize the set of points
    number_of_points = int(lines[0])
    data = lines[1:]
    points = []
    for i in range(number_of_points):
        datum = data[i].strip().split(" ")
        point = Point(float(datum[0]), float(datum[1]))
        points.append(point)

    # Brute force!!
    for i in range(number_of_points - 3):
        for j in range(i + 1, number_of_points - 2):
            for k in range(j + 1, number_of_points - 1):
                for l in range(k + 1, number_of_points):
                    # If the slopes of the four points are the same, they are on the same line
                    if (points[i].slope_to(points[j]) == points[i].slope_to(points[k])) and (
                            points[i].slope_to(points[j]) == points[i].slope_to(points[l])):
                        # Cute trick to get the first and last point of the line for plotting purposes
                        colinear_points = [points[i], points[j], points[k], points[l]]
                        colinear_points.sort()
                        print(f"{points[i]}, {points[j]}, {points[k]}, {points[l]}")
                        plot_colinear(colinear_points[0], colinear_points[-1])

    plot_points(points)
