class Point:

    # Constructor to take in x and y point coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Find the slope between two points
    def slope_to(self, b):
        delta_x = b.x - self.x
        if delta_x == 0.0:
            return float('inf')
        delta_y = b.y - self.y
        return delta_y / delta_x

    # Comparison function
    def __lt__(self, other):
        return self.x < other.x

    # Print to string
    def __str__(self):
        return f'({self.x}, {self.y})'
