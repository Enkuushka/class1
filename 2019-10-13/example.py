class Point:
    x = 0
    y = 0
    
    def __init__(self, xx=0, yy=0):
        self.x = xx
        self.y = yy

    def __add__(self, point2):
        _x = self.x + point2.x
        _y = self.y + point2.y
        return Point(_x, _y)

    def __str__(self):
        return "%d X %d"%(self.x, self.y)

class Point3D(Point):
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, point2):
        _x = self.x + point2.x
        _y = self.y + point2.y
        _z = self.z + point2.z
        return Point3D(_x, _y, _z)

    def __str__(self):
        return "%d X %d X %d"%(self.x, self.y, self.z)

p3d_1 = Point3D(4, 5, 6)
p3d_2 = Point3D(6, 5, 4)
p3d_3 = p3d_1 + p3d_2
print(p3d_3)