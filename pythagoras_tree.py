"""
Fractals https://mathworld.wolfram.com/topics/Fractals.html
Pythagoras tree https://demonstrations.wolfram.com/PythagorasTree/
"""
from square import Square
from point import Point
import math, random

def checked(lst):
    return [i for i in lst if i.lenA > 0.1 and i.lenB > 0.1]

def find_point(point1 : Point, point2 : Point , mode = -1 ) -> Point:    
    y_diff = point2.y - point1.y
    x_diff = point2.x - point1.x
    dis = math.sqrt((y_diff**2 + x_diff**2))
    tri_angle = math.pi/4 * mode 
    theata = math.atan2(point2.y-point1.y,point2.x-point1.x) + tri_angle
    height = math.sqrt(dis**2/2)
    x = height*math.cos(theata) + point1.x
    y = height*math.sin(theata) + point1.y
    return Point(x,y)

def make_square(basePoint,shared_point):
    angle = math.atan2(shared_point.y-basePoint.y,shared_point.x-basePoint.x)
    dis = math.sqrt((shared_point.y-basePoint.y)**2 + (shared_point.x-basePoint.x)**2)

    diagonal_dis = math.sqrt(dis**2*2)
    p1y = diagonal_dis * math.sin(angle - math.pi/4) + basePoint.y
    p1x = diagonal_dis * math.cos(angle - math.pi/4) + basePoint.x
    p1 = Point(p1x,p1y)

    p2y = dis * math.sin(angle - math.pi/2) + basePoint.y
    p2x = dis * math.cos(angle - math.pi/2) + basePoint.x
    p2 = Point(p2x,p2y)
    return Square(p1,p2,basePoint,shared_point)

def make_squares(angleA : float, base : Square) -> list[Square]: # takes only angleA as B is not needed

    
    dis = base.lenA
    normal_angle = math.atan2((base.p2.y-base.p1.y),(base.p2.x-base.p1.x)) 

    # find len a , b
    lenB = dis * math.sin(angleA)
    lenA = dis * math.cos(angleA)


    #calculate real angles 
    angleA += normal_angle
    # find shared point
    y_corr = lenA * math.sin(angleA) + base.p1.y
    x_corr = lenA * math.cos(angleA) + base.p1.x
    shared_point  = Point(x_corr,y_corr)

    # create squares

    # find squareA
    square_a = make_square(shared_point,base.p1)
    
    # find squareB
    square_b  = make_square(base.p2,shared_point)
   
    return checked([square_b, square_a])

def merge(lst1,lst2): 
    new_lst = []
    for i,j in zip(lst1, lst2):
        i.extend(j)
        new_lst.append(i)    
    return new_lst

def pythagoras_tree(base : Square, side_ratio : float, level : int) -> list[Square]:
    angleA = math.atan(  side_ratio)
    angleB = math.atan(1/side_ratio)
    """
    start square lst
    [
     [l1]
     [l2]
     [l3]
    ]

    """
    tree1 = [[base]]

    for i in range(1, level):
        tree1.append([])

        for square1 in tree1[i-1]:
            tree1[i].extend(make_squares(angleA,square1)) 
    
    #tree1.append(leaf)
    return tree1


def rlen(trees):
    count = 0
    for i in trees:
        if type(i) == list: count += rlen(i)
        else: count += 1
    return count


def make_trees(frames=3, level=10, start_ratio=1/1):
    trees = []
    # base square
    base = Square.flat(Point(0,0), Point(100,-100))
    # change of ratio
    # divide by frames//4 for symmetry
    incr = ((1)-start_ratio)/(frames//4)
    ratio = start_ratio
    print(f"{incr=}")
    for i in range(frames//2):
        print(f"{ratio=}")
        ratio += incr
        trees.append(pythagoras_tree(base,ratio, level))

    for i in range(frames//2):
        ratio -= incr
        trees.append(pythagoras_tree(base,ratio, level))

    return trees
