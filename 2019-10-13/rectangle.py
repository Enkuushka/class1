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

class Rectangle:
    topLeft = Point()
    rightBottom = Point()

    def setSize(self, urt, undor):
        self.rightBottom.x = self.rightBottom.x + urt
        self.rightBottom.y = self.rightBottom.y + undor


rect_1 = Rectangle()
print(rect_1.topLeft)


