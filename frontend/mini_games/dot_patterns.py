import random
import math


class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number


def populate_patterns():
    pattern_functions = [generate_rect_grid(), generate_spiral(), generate_random_dots()]
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


def generate_random_dots():
    random_dots = []
    current_number = 1
    for _ in range(20):
        x = random.randint(200, 1200)
        y = random.randint(200, 700)
        random_dots.append(Dot(x, y, current_number))
        current_number += 1
    return random_dots
