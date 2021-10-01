from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        selected_tuple=''
        index= list_box.curselection()[0]
        selected_tuple= list_box.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        print(selected_tuple)
    except IndexError:
        pass

def view_command():
    list_box.delete(0, END) 
    for row in backend.view():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    for row in backend.search(e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get()):
        list_box.insert(END, row)

def add_command():
    backend.insert(e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get())
    list_box.delete(0, END)
    list_box.insert(END, 'Succesfullly Added !' )
    list_box.insert(END, (e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get()) )

def update_command():
    backend.update(selected_tuple[0], e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get())
    list_box.delete(0, END)
    list_box.insert(END, 'Succesfullly Updated !' )
    list_box.insert(END, (e1_value.get(), e2_value.get(), e3_value.get(), e4_value.get()) )

def delete_command():
    list_box.delete(0, END)
    list_box.insert(END, 'Succesfullly Deleted !' )
    backend.delete(selected_tuple[0])

def clear_command():
    list_box.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

window = Tk()

window.wm_title('Book Library')

l1= Label(window, text= 'Title', font=('Times', 18, 'bold'))
l1.grid(row=0, column=0)

l2= Label(window, text= 'Author', font=('Times', 18, 'bold'))
l2.grid(row=0, column=2)

l3= Label(window, text= 'Year', font=('Times', 18, 'bold'))
l3.grid(row=1, column=0)

l4= Label(window, text= 'ISBN', font=('Times', 18, 'bold'))
l4.grid(row=1, column=2)

e1_value= StringVar()
e1= Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value= StringVar()
e2= Entry(window, textvariable=e2_value)
e2.grid(row=0, column=3)

e3_value= StringVar()
e3= Entry(window, textvariable=e3_value)
e3.grid(row=1, column=1)

e4_value= StringVar()
e4= Entry(window, textvariable=e4_value)
e4.grid(row=1, column=3)

list_box= Listbox(window, height=10, width=42)
list_box.grid(row=2, column=0, rowspan=7, columnspan=2)

scrl_bar= Scrollbar(window)
scrl_bar.grid(row=2, column=2, rowspan=7)

list_box.configure(yscrollcommand=scrl_bar.set)
scrl_bar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)


b1= Button(window, text= 'View All', command= view_command, height=1, width=15, font=('Times', 15, 'bold'))
b1.grid(row=2, column=3, padx=5, pady=5)
b2= Button(window, text= 'Serach a book', command=search_command, height=1, width=15, font=('Times', 15, 'bold'))
b2.grid(row=3, column=3, padx=5, pady=5)
b3= Button(window, text= 'Add a book', command=add_command, height=1, width=15, font=('Times', 15, 'bold'))
b3.grid(row=4, column=3, padx=5, pady=5)
b4= Button(window, text= 'Update Selected', command=update_command, height=1, width=15, font=('Times', 15, 'bold'))
b4.grid(row=5, column=3, padx=5, pady=5)
b5= Button(window, text= 'Delete Selected', command=delete_command, height=1, width=15, font=('Times', 15, 'bold'))
b5.grid(row=6, column=3, padx=5, pady=5)
b6= Button(window, text= 'Close', command=window.destroy, height=1, width=15, font=('Times', 15, 'bold'))
b6.grid(row=7, column=3, padx=5, pady=5)
b7= Button(window, text= 'Clear', command=clear_command, height=1, width=15, font=('Times', 15, 'bold'))
b7.grid(row=8, column=3, padx=5, pady=5)

window.mainloop()

