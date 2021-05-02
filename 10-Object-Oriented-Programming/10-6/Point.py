class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def move(self, x, y):
        self._x += x
        self._y += y

    def __repr__(self):
        return f'Point(x: {self.x}, y: {self.x})'

    def __str__(self):
        return f'x-coordinate: {self.x}, y-coordinate: {self.y}'


#p = Point(20, 30)
#print(p)
#p.move(50, 70)
#print(p)

