from tkinter import *

root = Tk()

root.geometry('{}x{}'.format(800, 600))

root.title("Search")

def noNothing():
    print("woot, nothing")

#layout for main containers

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='Search type', menu=subMenu)
subMenu.add_command(label='A* Search', command=noNothing)
subMenu.add_command(label='Breadth-First Search', command=noNothing)
menu.add_command(label='Start', command=noNothing)


search_frame = Frame(root, bg='pink')
search_frame.pack(fill=BOTH)


square = Canvas(search_frame)
isPressed = True

def click(event):
    isPressed = True
    if square.find_withtag(CURRENT):
        square.itemconfig(CURRENT, fill='yellow')

def unclick(event):
    isPressed = False
# square.create_rectangle(0, 0, 25, 25, fill='blue', outline='red', activefill='black')
                        #0, 0, 0+25, 0+25
# square.pack()
# square.create_rectangle(25, 0, 50, 25, fill='blue', outline='red', activefill='black')
                        #25, 0, +25, +25
# square.pack()
# square.create_rectangle(50, 0, 75, 25, fill='blue', outline='red', activefill='black')
# square.pack()
root.update_idletasks()
for y in range(800):
    for x in range(600):
        if x%25 == 0 and y%25 == 0:
            square.create_rectangle(x, y, x+25, y+25, fill='blue', outline='red')
square.pack(fill=BOTH)  

square.bind("<ButtonPress-1>", click)
square.bind("<ButtonRelease-1>", unclick)

# b = Canvas(top_frame, width=80, height=80, bg="pink", cursor="circle")
# b.pack()

# top_frame.pack()
root.mainloop()