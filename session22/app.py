import tkinter as tk
from tkinter import Message
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.05)  
        progress['value'] = i
        # Update the GUI
        root.update_idletasks()  
    progress.stop()

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)



root = tk.Tk()
root.title("My Window")

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=lambda: print('new manu'))
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

tk.Label(root, text="First Name").grid(row=0, column=0)
tk.Label(root, text="Last Name").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)



var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root, text="Male", variable=var1).grid(row=2, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=var2).grid(row=3, sticky=tk.W)





v = tk.IntVar()

tk.Radiobutton(root, text="A", variable=v, value=1).grid(row=4, column=0, sticky=tk.W)
tk.Radiobutton(root, text="B", variable=v, value=2).grid(row=4, column=1, sticky=tk.W)
tk.Radiobutton(root, text="C", variable=v, value=3).grid(row=4, column=2, sticky=tk.W)

tk.Label(root, text="Which language").grid(row=5, column=0)

lb = tk.Listbox(root)
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any other")

lb.grid(row=6, column=0)






label = tk.Label(root, text="Selected Item:")
label.grid(row=7, column=0)

# Create a Combobox widget
combo_box = ttk.Combobox(
    root,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly"
)
combo_box.grid(row=7, column=1)
combo_box.set("Option 1")
combo_box.bind("<<ComboboxSelected>>", select)






ourMessage = "This is our Message"
messageVar = Message(root, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.grid(row=8, column=0)


# Create a progressbar widget
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=9, column=0)

# Button to start progress
start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.grid(row=10, column=0)

root.mainloop()



 