from tkinter import *
from tkinter import filedialog
root=Tk()
root.title('Example of Menubar')
root.geometry('300x200')
label=Label(root,text='')
label.pack()
mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
Showmenu=Menu(mainmenu)
def open():
    label.configure(text='you have selected menu open')
    filedialog.askopenfilename()
filemenu.add_command(label='Open',command=open)
filemenu.add_separator()
filemenu.add_command(label='Close',command=root.destroy)
mainmenu.add_cascade(label='file',menu=filemenu)
root.config(menu=mainmenu)
root.mainloop()