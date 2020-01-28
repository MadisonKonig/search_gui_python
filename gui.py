import tkinter as tk
from tkinter import *
from bfs import *

root = Tk()

root.geometry('{}x{}'.format(500, 500))

root.title("Search")

all_points = []

square = Canvas(root, width=500, height=500)
square_size = 50
canvas_size = 500

#printing grid of squares

for y in range(canvas_size):
    for x in range(canvas_size):
        if x%square_size == 0 and y%square_size == 0:
            square.create_rectangle(x, y, x+square_size, y+square_size, fill='black', outline='white', tags='{},{}'.format(x,y))
            square.create_text((x+int(square_size/2), y+int(square_size/2)), text='{},{}'.format(x, y), fill='white')
square.pack(expand=True)  

def round_down(number, divisor):
    return (number - (number%divisor))

def noNothing():
    print("woot, nothing")

starting_coord = StringVar()
finishing_coord = StringVar()

def find_path(starting_point, goal_point, points_in_grid):
    return [['2,3'],['2,4'],['2,5']]


def start_this():
    # if starting_coord.get() != '':
    #     returned_points = find_path(starting_coord, finishing_coord, [])
    #     for x in range(len(returned_points)):
    #         print(returned_points[x][0])
    #         tmp = returned_points[x][0].split(',')
    #         square.itemconfig(square.find_closest((int(tmp[0]) * square_size), (int(tmp[1]) * square_size)), fill='pink')
    if starting_coord.get() != '':
        bfs = Bfs(starting_coord, finishing_coord, [], square, square_size)
        bfs.solve()
        

def two_points():
    print("hi")
    window = Toplevel(root)
    start_text = Label(window, text='start(x,y)')
    start_text.pack()
    # starting_coord = StringVar()
    start_value = Entry(window, textvariable=starting_coord, bd=1)
    start_value.pack()

    finish_text = Label(window, text='start(x,y)')
    finish_text.pack()
    # finishing_coord = StringVar()
    finish_value = Entry(window, textvariable=finishing_coord, bd=1)
    finish_value.pack()

    def close_and_save():
        window.destroy()
        starting_points = (starting_coord.get()).split(',')
        finishing_points = (finishing_coord.get()).split(',')
        square.itemconfig(square.find_closest((int(starting_points[0]) * square_size), (int(starting_points[1]) * square_size)), fill='pink')
        square.itemconfig(square.find_closest((int(finishing_points[0]) * square_size), (int(finishing_points[1]) * square_size)), fill='pink')

    b = tk.Button(window, text='Save', command=close_and_save)

    
    
    b.pack(side=BOTTOM)
    

#Layout for menu
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Search type', menu=subMenu)
subMenu.add_checkbutton(label='A* Search', command=noNothing)
subMenu.add_checkbutton(label='Breadth-First Search', command=noNothing)
menu.add_command(label='Points', command=two_points)
menu.add_command(label='Start', command=start_this)


#functions for clicking a square


def click(event):
    if square.find_withtag(CURRENT):
        # square.itemconfig(CURRENT, fill='green')
        print(event)



def unclick(event):
    # square.itemconfigure(square.find_closest(round_down(event.x, 50), round_down(event.x, 50)), fill='green')
    print(event)

def coords(event):
    square.itemconfig(square.find_closest(round_down(event.x, square_size), round_down(event.y, square_size)), fill='green')
    print('{}, {}'.format(round_down(event.x, square_size), round_down(event.y, square_size)))

        


            

square.bind("<Button-1>", click)
square.bind("<ButtonRelease-1>", unclick)
square.bind("<B1-Motion>", coords)

root.mainloop()


"""
so, I just need an array of how big the 2d array is, and pass that into a function.  
I'll already have the starting point, and the end point
the function will calcuate the route needed
and return an array of nodes that will need to change color in order for this is make sense

"""
"""
for having it show what nodes it tries as it moves along, I'll need...not actually sure on that one
"""