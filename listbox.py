from tkinter import *
def on_select(event): 
    selected_item = listbox.get(listbox.curselection()) 
    print(f"Selected item: {selected_item}") 
root = Tk() 
root.title("Listbox Example") 
root.geometry("400x200") 
listbox = Listbox(root) 
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]: 
    listbox.insert(END, item) 
listbox.bind('<<ListboxSelect>>', on_select) 
listbox.pack() 
root.mainloop() 