from square import Square
from draw import draw_move
from cli import *
from pythagoras_tree import make_trees

def main(frames=300):
    print("Hi u wanna build a tree")
    frames = GetFrameNum()
    level = 10

    trees = make_trees(frames=frames, level=10, start_ratio=1/2)

    draw_move(trees, level, "red", "green")

if __name__ == '__main__':
    main()