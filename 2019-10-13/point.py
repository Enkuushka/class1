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

tseg_1 = Point(3, 5)
tseg_2 = Point(10, 20)

tseg_3 = tseg_1 + tseg_2
print(tseg_1)
print(tseg_2)
print(tseg_3)