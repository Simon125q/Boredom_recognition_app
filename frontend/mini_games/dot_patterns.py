import random
import math


class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number


def populate_patterns():
    pattern_functions = [generate_rect_grid(), generate_spiral(), generate_concentric_circles(), generate_diamond_grid()]
    patterns = []
    for pattern_func in pattern_functions:
        patterns.append(pattern_func)
    return patterns


def generate_rect_grid():
    center_x = 700
    center_y = 400
    grid_size = 150

    num_rows = 5
    num_cols = 5

    start_x = center_x - (num_cols // 2) * grid_size
    start_y = center_y - (num_rows // 2) * grid_size

    grid = []
    current_number = 1
    for row in range(num_rows):
        for col in range(num_cols):
            x = start_x + col * grid_size
            y = start_y + row * grid_size
            grid.append(Dot(x, y, current_number))
            current_number += 1
    return grid


def generate_spiral():
    center_x = 700  # Fixed center x-coordinate
    center_y = 400  # Fixed center y-coordinate
    radius_increment = 18
    angle_increment = 1.2

    spiral_dots = []
    radius = 0

    current_number = 1
    for i in range(20):
        angle = i * angle_increment
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        spiral_dots.append(Dot(int(x), int(y), current_number))

        current_number += 1
        radius += radius_increment

    return spiral_dots

def generate_concentric_circles():
    center_x = 700
    center_y = 400
    num_circles = 5
    num_dots_per_circle = 12

    concentric_dots = []
    for i in range(num_circles):
        radius = 50 * (i + 1)
        for j in range(num_dots_per_circle):
            angle = j * (2 * math.pi / num_dots_per_circle)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            concentric_dots.append(Dot(int(x), int(y), (i * num_dots_per_circle) + j + 1))

    return concentric_dots


def generate_diamond_grid():
    center_x = 700
    center_y = 400
    grid_size = 100
    num_rows = 5
    num_cols = 5

    diamond_dots = []
    for row in range(num_rows):
        for col in range(num_cols):
            x = center_x + (col - num_cols // 2) * grid_size
            y = center_y + (row - num_rows // 2) * grid_size
            if (row + col) % 2 == 0:
                diamond_dots.append(Dot(x, y, len(diamond_dots) + 1))

    return diamond_dots
