from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling prompt

import os, glob, uuid
from moviepy.editor import *
from pygame.locals import *
from utills import FindBoundingBoxSize, flip_tree,FindBoundingBox
from cli import GetFileName, percent
from square import Square


pygame.init()
clock = pygame.time.Clock()

def done():
    pygame.quit()




def __centerPoints(points : list, xoff = 0, yoff = 0) -> list:
    # return centered points
    try:
        return [i + (xoff, yoff) for i in points]
    except Exception as e:
        print(points)
        raise e


def __hex_to_rgb(hex: str) -> tuple:
    rgb = []
    for i in range(1,6,2):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)


def treeify(tree_list):
    for index,i in  enumerate(tree_list):
        if type(i) != list: tree_list[index] = [i]



def draw_move(trees_list, level, c1, c2):
    tree_list = treeify(trees_list)

    flags = DOUBLEBUF|HIDDEN
    tree_list  = trees_list[0]
    flip_tree(tree_list)
   # get win
    xboarder, yboarder = 50, 50
    win = pygame.display.set_mode(FindBoundingBoxSize.squares(tree_list,xboarder,yboarder), flags )
    
    #find xoff, yoff
    width, height = pygame.display.get_surface().get_size()
    xoff, yoff = FindBoundingBox.squares(tree_list).center
    xoff = (width   - xoff+xboarder) /2
    yoff = (height  - yoff+yboarder) /2

    # find gradient
    from colour import Color
    red = Color("red")
    colours = [__hex_to_rgb(i.hex_l) for i in list(red.range_to(Color("green"),level))] 
    
    # make dir for temp files
    out_file = f"./out-{uuid.uuid4()}"
    os.mkdir(out_file)

    # render frames
    for fnum, tree_list in enumerate(trees_list):
        percent(fnum,len(trees_list),title="Rendering Frames please wait")
        win.fill((255,255,255))
        flip_tree(tree_list)
        for index, square_list in enumerate(tree_list):
            for i in square_list:
                colour = colours[index//2]
                if type(i) == Square:
                    pygame.draw.polygon(win,colour,__centerPoints(i.all,xoff,yoff))
                else:
                    pygame.draw.polygon(win,colour,i.all)
        pygame.display.flip()
        clock.tick(15)
        pygame.image.save_extended(win, f"{out_file}/frame{fnum}.png")

    # load all frames images and del
    imgs = []
    for filename in glob.glob("{out_file}/*.png"):
        img = ImageClip(filename).set_duration(0.01)
        os.remove(filename)
        imgs.append(img)
    # del temp dir
    os.rmdir(out_file)

    # get file name for video
    filename = GetFileName()
    # covert frames to vis

    video = concatenate(imgs, method="compose")
    video.fps = 30
    video.write_videofile(filename)
     


    print(f"Done, Video save in {filename}")
    video.preview()

    






    
