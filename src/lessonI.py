import math

class LessonI:
    id = None
    is_open = None

    def __init__(self, id):
        self.is_open = False
        self.id = id

    def naive(a, b):
        x = a
        y = b
        z = 0
        while x > 0:
            z = z + y
            x = x - 1
        return z

    def time(n):
        """ Return the number of steps
        necessary to calculate
        `print countdown(n)`"""
        steps = 0
        # YOUR CODE HERE

        steps = 3 + math.ceil(n / 5.0) * 2;

        return steps


