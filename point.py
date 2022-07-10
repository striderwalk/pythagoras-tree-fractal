from typing import NamedTuple


class Point(NamedTuple):
    """
    a simplified vector
    """
    x : int
    y : int

    def __mul__(self, num) :
        if isinstance(num, int): return Point(self.x * num, self.y * num)
        if isinstance(num, float): return Point(self.x * num, self.y * num)
        if isinstance(num, tuple): return Point(self.x * num[0], self.y * num[1])
    def __truediv__ (self, num) :
        if isinstance(num, int): return Point(self.x / num, self.y / num)
        if isinstance(num, float): return Point(self.x / num, self.y / num)
        if isinstance(num, tuple): return Point(self.x / num[0], self.y / num[1])
    def __add__(self, num) :
        if isinstance(num, int): return Point(self.x + num, self.y + num)
        if isinstance(num, float): return Point(self.x + num, self.y + num)
        if isinstance(num, tuple): return Point(self.x + num[0], self.y + num[1])
    def __sub__(self, num) :
        if isinstance(num, int): return Point(self.x - num, self.y - num)
        if isinstance(num, float): return Point(self.x - num, self.y - num)
        if isinstance(num, tuple): return Point(self.x - num[0], self.y - num[1])

    def ToInt(self): return (int(self.x),int(self.y))