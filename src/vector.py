import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE = "Cannot normalize vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __add__(self, other):
        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)]);

    def __sub__(self, other):
        return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)]);

    def times_scalar(self, c):
        return Vector([Decimal(c) * x for x in self.coordinates]);

    def magnitude(self):
        return Decimal(math.sqrt(math.fsum(math.pow(x, 2) for x in self.coordinates)))

    def is_null_vector(self, tolerance=1e-10):
        return abs(self.magnitude()) < tolerance;

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE)

    def dot_product(self, other):
        return sum([x * y for x,y in zip(self.coordinates, other.coordinates)])

    def angle(self, other, is_degree=False):
        try:
            norm_dot = self.normalize().dot_product(other.normalize());

            if norm_dot >= 1:
                angle = math.acos(1)
            elif norm_dot <= -1:
                angle = math.acos(-1)
            else:
                angle = math.acos(norm_dot)

            return math.degrees(180 * angle / math.pi) if is_degree else angle
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE:
                raise ("cannot compute angle for 0 vector")
            else:
                raise e

    def is_parallel(self, other):
        if self.is_null_vector() or other.is_null_vector():
            return True

        degree = self.angle(other, True)
        return degree == 0 or degree == 180

    def is_orthogonal(self, other, tolerance=1e-10):
        if self.is_null_vector() or other.is_null_vector():
            return True

        return abs(self.dot_product(other)) < tolerance;

    def proj(self, other):
        norm_other = other.normalize();
        length = self.dot_product(norm_other);
        return norm_other.times_scalar(length);

    def check_crossproduct_vector(self):
        if len(self.coordinates) > 3 or len(self.coordinates) < 2:
            raise ("not supported")

        if len(self.coordinates) == 2:
            self.coordinates = tuple(list(self.coordinates).append(Decimal(1.0)));

        return self

    def cross_product(self, other):
        v = self.check_crossproduct_vector()
        w = other.check_crossproduct_vector()

        #ilyet is lehet?:D
        #x_1, y_1, z_1 = self.coordinates
        #x_2, y_2, z_2 = other.coordinates

        i = self.coordinates[1] * other.coordinates[2] - self.coordinates[2] * other.coordinates[1]
        j = self.coordinates[0] * other.coordinates[2] - self.coordinates[2] * other.coordinates[0]
        k = self.coordinates[0] * other.coordinates[1] - self.coordinates[1] * other.coordinates[0]

        return Vector([i, -j, k])

    def parallelogram_area(self, other):
        return self.cross_product(other).magnitude()

    def triangle_area(self, other):
        return self.parallelogram_area(other) / 2

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
