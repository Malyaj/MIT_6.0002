# Hello World program in Python

class point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({i}, {j})".format(i=self.x, j=self.y)
    
    def distanceFrom(self, otherPoint):
        '''assuming that otherPoint is a Point object'''
        return ((self.x - otherPoint.x) ** 2 + (self.y - otherPoint.y) ** 2) ** 0.5

    def distanceFromOrigin(self):
        otherPoint = point(0,0)
        return ((self.x - otherPoint.x) ** 2 + (self.y - otherPoint.y) ** 2) ** 0.5
    
    def quadrane(self):
        pass
    

p1 = point(2, 3)
p2 = point(10, -1)

def distanceBetween(p1, p2):
    '''assuming p1 and p2 are both point objects'''
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

print("Distance between points {p1} and {p2} is {dis}".format(p1=p1, p2=p2, dis=distanceBetween(p1,p2)))

print("-+-" * 30)
