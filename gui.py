from tkinter import *

root = Tk()

root.geometry('{}x{}'.format(800, 600))

root.title("Search")

#layout for main containers
top_frame = Frame(root, bg='blue', width=800, height=50)
search_frame = Frame(root, bg='pink', width=800, height=550)

top_frame.grid(row=0)
search_frame.grid(row=1)

#the list of search types
search_list = [
    'A* search',
    'Breadth-first search'
]
variable_of_search = StringVar(root)
variable_of_search.set(search_list[0])

#widgets for top frame
search_label = Label(top_frame, text='Type') #search_type.current() for the current index
search_type = OptionMenu(top_frame, variable_of_search, *search_list)
# prompt_for_start = 

search_label.grid(row=0, column=0)
search_type.grid(row=0, column=1)

# b = Canvas(top_frame, width=80, height=80, bg="pink", cursor="circle")
# b.pack()

# top_frame.pack()
root.mainloop()