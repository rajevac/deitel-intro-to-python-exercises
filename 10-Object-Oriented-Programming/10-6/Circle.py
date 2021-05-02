from Point import Point


class Circle:

    def __init__(self, radius, point=None):
        if point is None:
            point = [0, 0]
        self.radius = radius
        self.point = point

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        x, y = point
        self._point = Point(x, y)

    def move(self, x, y):
        self.point.move(x, y)

    def __repr__(self):
        return f'Circle(radius: {self.radius}, Point: {self.point})'

    def __str__(self):
        return f'circle radius: {self.radius}, circle-center-coordinates: {self.point}'


c = Circle(50, [10, 10])
print(c)
c.move(20, 15)
print(c)



