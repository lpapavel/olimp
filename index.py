from tkinter import *
import math

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

def create_vertical_lines(canvas, f_height, f_width, sector_size):
    # vertical
    vertical_mid_list = []
    count = 0
    step = sector_size
    n = 0
    while count < f_width:
        canvas.create_line(count, 0, count, f_height)
        count = count + step
        n = n + 1
        current_mid = (step * n) - (step / 2)
        vertical_mid_list.append(current_mid)
    return vertical_mid_list


def create_horizontal_lines(canvas, f_height, f_width, sector_size):
    # horisontal
    horisontal_mid_list = []
    step = sector_size
    n = 0
    count = 0
    while count < f_height:
        canvas.create_line(0, count, f_width, count)
        count = count + step
        n = n + 1
        current_mid = (step * n) - (step / 2)
        horisontal_mid_list.append(current_mid)
    return horisontal_mid_list


def get_copter_params():
    print("========== - COPTER PARAMS - ==========")
    cam_view_angle = input("Enter cam angle: ")
    flight_altitude = input("Enter the flight altitude: ")

    return cam_view_angle, flight_altitude


def calculate_sector_size(angle, altitude):
    ang = (math.pi / 3) / 2 # 1/2 of alfa angle (for calculating size of the sector) TAN(alpha) = 1/2 sector size / height

    result = 2 * altitude * math.tan(ang)
    return round(result)


def create_sectors(canvas, f_height, f_width):

    (cam_view_angle, flight_altitude) = get_copter_params()

    sector_size = calculate_sector_size(int(cam_view_angle), int(flight_altitude))

    vertical_mid_list = []
    horizontal_mid_list = []

    vertical_mid_list = create_vertical_lines(canvas, f_height, f_width, sector_size)
    horizontal_mid_list = create_horizontal_lines(canvas, f_height, f_width, sector_size)

    return vertical_mid_list, horizontal_mid_list


tkinter = Tk()

(canv_height, canv_width) = get_canv_params()
canv = create_canvas(canv_height, canv_width, tkinter) # Drawing canvas
canv.pack()

(field_height, field_width) = create_field(canv, canv_height, canv_width) # Drawing field

(vertical_mid_list, horizontal_mid_list) = create_sectors(canv, field_height, field_width) # Drawing sectors (step = 10px default) !!!!! -- > mid_lists - list with mid coords




tkinter.mainloop()