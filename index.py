from tkinter import *
import math

def get_canv_params():
    #print("========== - DRAWING CANVAS - ==========")
    #height = input("[ ! ] Enter canvas height: ")
    #width = input("[ ! ] Enter canvas width: ")
    return 9000, 9000

def create_canvas(_width, _height,tkinter):
    canv = Canvas(tkinter, width=_width, height=_height, bg='white')
    return canv

def create_field(canvas, c_height, c_width):
    print("\n========== - DRAWING FIELD - ==========")
    width1 = input("[ ! ] Enter longitude0 : ")
    height1 = input("[ ! ] Enter latitude0 : ")

    width2 = input("[ ! ] Enter longitude (end) : ")
    height2 = input("[ ! ] Enter latitude (end) : ")

    height = height2 - height1
    width = width2 - width1

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

def print_dots(vertical_mid_list, horizontal_mid_list, canvas, width, height):
    element = 0
    count = 0
    while count < vertical_mid_list.__len__():
        while element < horizontal_mid_list.__len__():
            canvas.create_line(vertical_mid_list[count], horizontal_mid_list[element], vertical_mid_list[count], horizontal_mid_list[element] + 1)
            element = element + 1
        count = count + 1
        element = 0

def print_way(canvas, horizontal_mid_list, vertical_mid_list):
    count = 0
    row = 0
    count_max = vertical_mid_list.__len__()
    row_max = horizontal_mid_list.__len__()
    while count < vertical_mid_list.__len__() - 1:
        while row < horizontal_mid_list.__len__():
            canvas.create_line(horizontal_mid_list[row], vertical_mid_list[count], horizontal_mid_list[row - 1],
                               vertical_mid_list[count], arrow=FIRST)
            row = row + 1

        canvas.create_line(horizontal_mid_list[row - 1], vertical_mid_list[count], horizontal_mid_list[0],
                           vertical_mid_list[count + 1])
        row = 0
        count = count + 1

    while row < horizontal_mid_list.__len__() - 1:
        canvas.create_line(horizontal_mid_list[row], vertical_mid_list[count_max - 1], horizontal_mid_list[row + 1],
                           vertical_mid_list[count_max - 1], arrow=LAST)
        row = row + 1

    # go home
    canvas.create_line(horizontal_mid_list[row_max - 1], vertical_mid_list[count_max - 1], horizontal_mid_list[0], vertical_mid_list[0])

def change_optimal_way(canv, horizontal_mid_list, vertical_mid_list):
    x_len = horizontal_mid_list.__len__()
    y_len = vertical_mid_list.__len__()

    if x_len % 2 == 0 and y_len % 2 == 1:
        print("Var - 1")

        print("Var - 1")
    elif x_len % 2 == 1 and y_len % 2 == 0:
        print("V - 2")
    elif x_len % 2 == 1 and y_len % 2 == 1:
        print("V - 3")


def export_x(h_m_l):
    count = 0
    output_x = open("output_x.txt", 'w')
    while count < h_m_l.__len__():
        output_x.write(str(h_m_l[count]) + "\n")
        count = count + 1
    output_x.close()
    print("[ ! ] X coordinates were exported to -- > output_x.txt \n")

def export_y(v_m_l):
    count = 0
    output_y = open("output_y.txt", 'w')
    while count < v_m_l.__len__():
        output_y.write(str(v_m_l[count]) + "\n")
        count = count + 1
    output_y.close()
    print("[ ! ] Y coordinates were exported to -- > output_y.txt \n")

def export_coordinates(h_m_l , v_m_l):
    export_x(horizontal_mid_list)
    export_y(vertical_mid_list)

def optimal_way_1(canvas, horizontal_mid_list, vertical_mid_list):
    y = 0
    x = 0
    output_c = open("output.txt", 'w')
    output_c.write("X  :  Y \n")

    while y < vertical_mid_list.__len__() - 1:
        canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x], vertical_mid_list[y + 1], arrow=LAST)
        output_c.write(str(horizontal_mid_list[x]) + " : " + str(vertical_mid_list[y]) + "\n")
        y = y + 1


    while x < horizontal_mid_list.__len__() - 1:
        canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x + 1], vertical_mid_list[y], arrow=LAST)
        x = x + 1
        output_c.write(str(horizontal_mid_list[x]) + " : " + str(vertical_mid_list[y])+ "\n")

    canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x], vertical_mid_list[y - 1], arrow=LAST)
    output_c.write(str(horizontal_mid_list[x]) + " : " + str(vertical_mid_list[y]) + "\n")


    y = y - 1
    top_turn = True

    count = 0

    while count < (horizontal_mid_list.__len__() - 1) / 2:
        while y > 0:
            canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x],
                               vertical_mid_list[y - 1], arrow=LAST)
            y = y - 1
        canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x - 1],
                           vertical_mid_list[y], arrow=LAST)
        x = x - 1
        y = 0
        while y < vertical_mid_list.__len__() - 2:
            canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x],
                               vertical_mid_list[y + 1], arrow=LAST)
            y = y + 1
        canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x - 1],
                           vertical_mid_list[y], arrow=LAST)
        x = x - 1

        count = count + 1
    #### go top

    while y > 0:
        canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x],
                           vertical_mid_list[y - 1], arrow=LAST)
        y = y - 1

    #### go home

    canvas.create_line(horizontal_mid_list[x], vertical_mid_list[y], horizontal_mid_list[x - 1],
                       vertical_mid_list[y], arrow=LAST)




tkinter = Tk()

(canv_height, canv_width) = get_canv_params()
canv = create_canvas(canv_height, canv_width, tkinter) # Drawing canvas
canv.pack()

(field_height, field_width) = create_field(canv, canv_height, canv_width) # Drawing field

(vertical_mid_list, horizontal_mid_list) = create_sectors(canv, field_height, field_width) # Drawing sectors (step = 10px default) !!!!! -- > mid_lists - list with mid coords

print_dots(vertical_mid_list, horizontal_mid_list, canv, field_width, field_height)

#export_coordinates(vertical_mid_list, horizontal_mid_list)

#print_way(canv, vertical_mid_list, horizontal_mid_list) # Default not optimal way

change_optimal_way(canv, vertical_mid_list, horizontal_mid_list)

optimal_way_1(canv, vertical_mid_list, horizontal_mid_list)

tkinter.mainloop()