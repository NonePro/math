import math
import matplotlib.pyplot as plt
import numpy as np


def distribute_points_on_circle(num_points, radius, rotate=0):
    """Returns a list of points evenly distributed on a circle."""
    points = []
    angle = 360 / num_points
    for i in range(num_points):
        curr_angle = i * angle + rotate
        x = math.cos(math.radians(curr_angle)) * radius
        y = math.sin(math.radians(curr_angle)) * radius
        points.append((x, y))
    return points


def circle_points(radius=5):
    # Define the center and radius of the circle
    x0, y0 = 0, 0

    # Generate array of angles
    theta = np.linspace(0, 2 * np.pi, 100)

    # Calculate x and y coordinates of circle
    x = x0 + radius * np.cos(theta)
    y = y0 + radius * np.sin(theta)

    return x, y


if __name__ == '__main__':
    # Usage example
    points = distribute_points_on_circle(13, 5, False)
    points += [points[0]]
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    plt.plot(x_coords, y_coords)

    # Plot the circle and set aspect ratio to be equal
    plt.plot(*circle_points(5))

    plt.axis('equal')
    plt.show()
