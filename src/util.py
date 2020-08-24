"""
Provides miscellaneous functionality, like vectors
"""


class Vec2:
    """
    Implements all common operations on vectors in R2.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vec2({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Vec2):
            return False

        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other

        return self

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other

        return self

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y

        raise IndexError("Index out of range.")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value
            return

        raise IndexError("Index out of range.")

    def copy(self):
        '''
        Copies the current vector and returns a new one
        '''
        return Vec2(self.x, self.y)

    def element_mul(self, other):
        '''
        Multiplies two vectors element-wise
        '''
        return Vec2(self.x * other.x, self.y * other.y)

    def dot(self, other):
        '''
        Returns the dot product of two vectors.
        '''
        return self.x * other.x + self.y * other.y

    def no_root_norm(self):
        '''
        Calculates the norm of the vector without taking the square root. This
        is useful for quickly comparing two vectors, when the actual length
        isn't important.
        '''

        return self.x ** 2 + self.y ** 2

    def norm(self):
        '''
        Calculates the norm or length of the vector.
        '''
        return self.no_root_norm() ** 0.5

    def normalize(self):
        '''
        Return a new vector representing the normalized current vector.
        '''
        norm = self.norm()
        return Vec2(self.x / norm, self.y / norm)

    def normalize_inplace(self):
        '''
        Normalize the current vector in place, doesn't create a new vector.
        '''
        norm = self.norm()

        self.x /= norm
        self.y /= norm

        return self
