from tkinter import *

# Window creation and labeling
calc = Tk()
calc.title("Calculator")
calc.resizable(width=0, height=0)

# Screen define and add
screen = Entry(calc, width=30, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

global f_num
global math


# Button actions
def button_click(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))


def button_clear():
    screen.delete(0, END)


def button_add():
    first_number = screen.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "addition"
    screen.delete(0, END)


def button_sub():
    first_number = screen.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "subtraction"
    screen.delete(0, END)


def button_mul():
    first_number = screen.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "multiplication"
    screen.delete(0, END)


def button_div():
    first_number = screen.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "division"
    screen.delete(0, END)


def button_equal():
    second_number = screen.get()
    screen.delete(0, END)
    if math == "addition":
        screen.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        screen.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        screen.insert(0, f_num * float(second_number))
    elif math == "division":
        screen.insert(0, f_num / float(second_number))


# Define buttons

button_1 = Button(calc, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(calc, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(calc, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(calc, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(calc, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(calc, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(calc, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(calc, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(calc, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(calc, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_mul = Button(calc, text="*", padx=38, pady=20, command=button_mul)
button_dot = Button(calc, text=".", padx=42, pady=20, command=lambda: button_click("."))
button_equ = Button(calc, text="=", padx=38, pady=20, command=button_equal)
button_add = Button(calc, text="+", padx=36, pady=20, command=button_add)
button_sub = Button(calc, text="-", padx=39, pady=20, command=button_sub)
button_div = Button(calc, text="/", padx=39, pady=20, command=button_div)
button_clear = Button(calc, text="clear", padx=26, pady=20, command=button_clear)

# Put buttons on screen

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equ.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=0, column=3)

calc.mainloop()
