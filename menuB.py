from tkinter import *
root=Tk()
root.title('Example of MenuButtons')
root.geometry('300x250')
def show_menu():
    print(f'option Checked:{var.get()}')
menubutton=Menubutton(root,text='Options')
menubutton.pack(pady=20)
menu=Menu(menubutton,tearoff=0)
menubutton['menu']=menu
var=IntVar(value=0)
menu.add_checkbutton(label='Check Me',variable=var,command=show_menu)
root.mainloop() 