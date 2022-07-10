from point import Point
import math

class Square:
    """
    takes two opisite points on a square
             a
              ■
               b
    finds other two points and groups by side 
    really a rect but square is a better word
    """
    @classmethod
    def flat(self, p1 : Point, p3 : Point):
        p1 = Point(*p1)
        p2 = Point(p3[0], p1[1])
        p3 = Point(*p3)
        p4 = Point(p1[0], p3[1])
        return Square(p1,p2,p3,p4)

    def __init__(self, p1 : Point, p2 : Point, p3 : Point, p4 : Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def rotate_points_left(self): self.p1,self.p2,self.p3,self.p4 = self.p4,self.p1,self.p2,self.p3
    def rotate_points_right(self): self.p1,self.p2,self.p3,self.p4 =  self.p2,self.p3,self.p4,self.p1
    def flip(self): 
        self.p1 *= -1
        self.p2 *= -1
        self.p3 *= -1
        self.p4 *= -1
    def __repr__(self): return f"Square at {self.all}"
    @property
    def center(self):
        return Point((self.p1.x+self.p2.x+self.p3.x+self.p4.x)/4,(self.p1.y+self.p2.y+self.p3.y+self.p4.y)/4)     
    @property
    def top(self):
        return [self.p1, self.p2]
    @property
    def right(self):
        return [self.p2, self.p3]
    @property
    def bottom(self):
        return [self.p3, self.p4]
    @property
    def left(self):
        return [self.p4, self.p1]
    @property
    def all(self):
        return [self.p1,self.p2,self.p3,self.p4]
    @property
    def lenA(self): # returns dis bettewn p1,p2
        return math.sqrt((self.p2.y-self.p1.y)**2+(self.p2.x-self.p1.x)**2)
    @property
    def lenB(self): # # returns dis bettewn p2,p3 
        return math.sqrt((self.p3.y-self.p2.y)**2+(self.p3.x-self.p2.x)**2)