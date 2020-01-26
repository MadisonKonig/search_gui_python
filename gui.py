from tkinter import *

root = Tk()

root.geometry('{}x{}'.format(600, 600))

root.title("Search")

def noNothing():
    print("woot, nothing")

#Layout for menu
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='Search type', menu=subMenu)
subMenu.add_command(label='A* Search', command=noNothing)
subMenu.add_command(label='Breadth-First Search', command=noNothing)
menu.add_command(label='Start', command=noNothing)

#functions for clicking a square
square = Canvas(root, width=600, height=600)

def click(event):
    if square.find_withtag(CURRENT):
        square.itemconfig(CURRENT, fill='yellow')
    print(event)



def unclick(event):
    print(event)

def coords(event):
    if(event.x%25 == 0 or event.y%25 == 0):
        print(square.find_withtag("{},{}".format(event.x,event.y)).config(fill='yellow'))
        # print(square.gettags(square.find_withtag(CURRENT)))
        # square.itemconfig(ACTIVE, fill='yellow')
        # print(event.widget.configure(background='yellow'))
        

#printing grid of squares

for y in range(600):
    for x in range(600):
        if x%25 == 0 and y%25 == 0:
            square.create_rectangle(x, y, x+25, y+25, fill='black', outline='white', tags='{},{}'.format(x,y))
square.pack(expand=True)  

# square.bind("<Button-1>", click)
square.bind("<ButtonRelease-1>", unclick)
square.bind("<B1-Motion>", coords)

root.mainloop()