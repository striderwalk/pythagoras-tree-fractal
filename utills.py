from square import Square
from point import Point
class FindBoundingBox:
    @staticmethod
    def squares(tree_list):
        minX, minY, maxX,maxY = 300000,300000,0,0
        for squares_list in tree_list:
            for square in squares_list:
                if type(square) != Square: continue
                for point in square.all:
                    if point.x < minX: minX = point.x
                    if point.y < minY: minY = point.y
                    if point.x > maxX: maxX = point.x
                    if point.y > maxY: maxY = point.y
        return Square.flat(Point(minX,minY),Point(maxX,maxY))
    @staticmethod
    def points(point_list):
        minX, minY, maxX,maxY = 30000,30000,0,0
        for lst in point_list:
            for point in lst:
                if point.x < minX: minX = point.x
                if point.y < minY: minY = point.y
                if point.x > maxX: maxX = point.x
                if point.y > maxY: maxY = point.y
        return Square.flat(Point(minX,minY),Point(maxX,maxY))

class FindBoundingBoxSize:
    @staticmethod
    def squares(tree_list, xboarder=0,yboarder=0):
        minX, minY, maxX,maxY = 300000,300000,0,0
        for squares_list in tree_list:
            for square in squares_list:
                if type(square) != Square: continue
                for point in square.all:
                    if point.x < minX: minX = point.x
                    if point.y < minY: minY = point.y
                    if point.x > maxX: maxX = point.x
                    if point.y > maxY: maxY = point.y
        return (abs(maxX-minX+xboarder*2),abs(maxY-minY+yboarder*2))
    @staticmethod
    def points(point_list, xboarder=0,yboarder=0):
        minX, minY, maxX,maxY = 30000,30000,0,0
        for lst in point_list:
            for point in lst:
                if point.x < minX: minX = point.x
                if point.y < minY: minY = point.y
                if point.x > maxX: maxX = point.x
                if point.y > maxY: maxY = point.y
        return (abs(maxX-minX+xboarder*2),abs(maxY-minY+yboarder*2))

def flip_tree(tree_list):
    import copy
    for squares_list in tree_list:
            for index, square in enumerate(squares_list):
                if index == 0:
                    squares_list[0] = copy.deepcopy(square)
                    
                    squares_list[0].flip()

                else:
                    square.flip()
                    

