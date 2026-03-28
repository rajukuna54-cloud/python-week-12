from tkinter import *
from tkinter import messagebox, filedialog
root = Tk()
root.title('Example Messagebox and File Dialog')
root.geometry('400x300')
def show_message():
    messagebox.showinfo('Information','Hello! This is a Message Box')
def open_file():
    file = filedialog.askopenfilename(
        title='Select a File',
        filetypes=(('Text Files', '*.txt'), ('All Files', '*.*'))
    )
    if file:
        messagebox.showinfo('Selected File', file)
def save_file():
    file = filedialog.asksaveasfilename(
        title='Save File',
        defaultextension='.txt',
        filetypes=(('Text Files','*.txt'), ('All Files', '*.*'))
    )
    if file:
        messagebox.showinfo('File Saved', file)
Button(root, text='Show Message', command=show_message).pack(pady=10)
Button(root, text='Open File', command=open_file).pack(pady=10)
Button(root, text='Save File', command=save_file).pack(pady=10)
root.mainloop()