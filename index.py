from tkinter import *

def get_canv_params():
    print("========== - DRAWING CANVAS - ==========")
    height = input("[ ! ] Enter canvas height: ")
    width = input("[ ! ] Enter canvas width: ")
    return height, width

def create_canvas(_width, _height,tkinter):
    canv = Canvas(tkinter, width=_width, height=_height, bg='white')
    return canv

def create_field(canvas, c_height, c_width):
    print("\n========== - DRAWING FIELD - ==========")
    height = input("[ ! ] Enter field height: ")
    width = input("[ ! ] Enter field width: ")
    if height < c_height and width < c_width:
        canvas.create_rectangle(0, 0, width, height)
        return height, width
    else:
        while height > c_height or width > c_width:
            print("Incorrect data ! Try again")
            height = input("[ ! ] Enter field height: ")
            width = input("[ ! ] Enter field width: ")
    canvas.create_rectangle(0, 0, width, height)
    return height, width

def create_vertical_lines(canvas, f_height, f_width):
    # vertical
    vertical_mid_list = []
    count = 0
    step = 10
    n = 0
    while count < f_width:
        canvas.create_line(count, 0, count, f_height)
        count = count + step
        n = n + 1
        current_mid = (step * n) - (step / 2)
        vertical_mid_list.append(current_mid)
    return vertical_mid_list


def create_horizontal_lines(canvas, f_height, f_width):
    # horisontal
    horisontal_mid_list = []
    step = 10
    n = 0
    count = 0
    while count < f_height:
        canvas.create_line(0, count, f_width, count)
        count = count + step
        n = n + 1
        current_mid = (step * n) - (step / 2)
        horisontal_mid_list.append(current_mid)
    return horisontal_mid_list


def create_sectors(canvas, f_height, f_width):

    vertical_mid_list = []
    horizontal_mid_list = []

    vertical_mid_list = create_vertical_lines(canvas, f_height, f_width)
    horizontal_mid_list = create_horizontal_lines(canvas, f_height, f_width)

    return vertical_mid_list, horizontal_mid_list


tkinter = Tk()

(canv_height, canv_width) = get_canv_params()
canv = create_canvas(canv_height, canv_width, tkinter) # Drawing canvas
canv.pack()

(field_height, field_width) = create_field(canv, canv_height, canv_width) # Drawing field

(vertical_mid_list, horizontal_mid_list) = create_sectors(canv, field_height, field_width) # Drawing sectors (step = 10px default) !!!!! -- > mid_lists - list with mid coords




tkinter.mainloop()