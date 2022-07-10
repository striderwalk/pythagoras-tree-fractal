from time import sleep
import os
import cv2



def percent(index, total, bar_len=50, title="Please wait"): # displays progress
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = "█"*int(done)
    togo_str = " "*int(togo)

    if done != 0:
        togo_str ="░" + togo_str[:-1]


    print(f'\u001b[2k⏳{title}: [{done_str}{togo_str}] {percent_done}% done', end='\r')

    if percent_done >= 100: print('\u001b[2\t✅')

def GetFrameNum():

    frame_num = input("How many frames would you like? \u001b[33;1m500\u001b[0m is good: ") # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#cursor-navigation
    try:
        frame_num = int(frame_num)
    except:
        print(f"{frame_num} is not a vaild number, 500 frames has been selected")
        frame_num = 500
    if 10000 < frame_num < 0:
        print(print(f"{frame_num} is not a vaild number, 500 frames has been selected"))
        frame_num = 500
    return frame_num

def GetFileName():
    # get diretory
    directory = input("Where would you like to save the file: ")
    if directory == "":
        print("No path specified will save in \u001b[33;1mTreeOut\u001b[0m")
        directory = "TreeOut"
    if not os.path.isdir(directory):
        print("path does not exists creating new folder: ")
        os.mkdir(directory)

    # get file name
    print("Your file be in the \u001b[33;1mmp4\u001b[0m format")
    filename = input("What would you like to name it? ").strip()
    if filename == "":
        print("No filename specified will save as \u001b[33;1mTrees\u001b[0m\n")
        filename = "Trees"

    if os.path.isfile(f"{directory}/{filename}"): raise FileExistsError


    return f"./{directory}/{filename}.mp4"


    


    
       

       
        
      



       


       





