import tkinter as tk 
root = tk.Tk() 
root.title("Scrollbar Example") 
root.geometry("400x200") 
listbox = tk.Listbox(root) 
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview) 
listbox.config(yscrollcommand=scrollbar.set) 
for i in range(100): 
    listbox.insert(tk.END, f"Item {i+1}") 
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 
scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
root.mainloop()