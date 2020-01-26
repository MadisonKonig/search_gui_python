from tkinter import *

root = Tk()

root.geometry('{}x{}'.format(500, 500))

root.title("Search")

square = Canvas(root, width=500, height=500)

def round_down(number, divisor):
    return (number - (number%divisor))

def noNothing():
    print("woot, nothing")

def start_this():
    print(square.find_all())

#Layout for menu
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='Search type', menu=subMenu)
subMenu.add_command(label='A* Search', command=noNothing)
subMenu.add_command(label='Breadth-First Search', command=noNothing)
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
    square.itemconfig(square.find_closest(round_down(event.x, 50), round_down(event.y, 50)), fill='green')
    print('{}, {}'.format(round_down(event.x, 50), round_down(event.y, 50)))
    # if(event.x%25 == 0 or event.y%25 == 0):
        # square.itemconfigure(square.find_closest(event.x, event.y), fill='yellow')

        

#printing grid of squares

for y in range(500):
    for x in range(500):
        if x%50 == 0 and y%50 == 0:
            square.create_rectangle(x, y, x+50, y+50, fill='black', outline='white', tags='{},{}'.format(x,y))
            square.create_text((x+25, y+25), text='{},{}'.format(x, y), fill='white')
square.pack(expand=True)  
            

square.bind("<Button-1>", click)
square.bind("<ButtonRelease-1>", unclick)
square.bind("<B1-Motion>", coords)

root.mainloop()