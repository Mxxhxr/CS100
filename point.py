import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)
    
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x 
        self.y += y

    def distance_to(self, otherPoint):
        xdiff = self.x - otherPoint.coordinates()[0]
        ydiff = self.y - otherPoint.coordinates()[1]
        return math.sqrt(xdiff**2 + ydiff**2)

