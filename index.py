from tkinter import * #importing all from tkinter

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
        canvas.create_rectangle(0, 0, height, width)
        return height, width
    else:
        while height > c_height or width > c_width:
            print("Incorrect data ! Try again")
            height = input("[ ! ] Enter field height: ")
            width = input("[ ! ] Enter field width: ")
    canvas.create_rectangle(0, 0, height, width)
    return height, width

def create_vertical_lines(canvas, f_height, f_width):
    step = 0
    while step < f_width:
        canvas.create_line(step, 0, step, f_height)
        step = step + 10

def create_horizontal_lines(canvas, f_height, f_width):
    step = 0
    while step < f_height:
        canvas.create_line(0, step, f_width, step)
        step = step + 10

def create_sectors(canvas, f_height, f_width):

    create_vertical_lines(canvas, f_height, f_width)
    create_horizontal_lines(canvas, f_height, f_width)

tkinter = Tk()

(canv_height, canv_width) = get_canv_params()

canv = create_canvas(canv_height, canv_width, tkinter)
canv.pack()

(field_height, field_width) = create_field(canv, canv_height, canv_width)

create_sectors(canv, field_height, field_width)

tkinter.mainloop()