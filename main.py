import tkinter as tk
from tkinter import * 
from tkinter.ttk import *

with open("q", "r", encoding="utf-8") as t:
            t = t.readlines()

root = tk.Tk()
root.attributes('-fullscreen',True)
root.title("The Pack Geometry Manager")
root.geometry("340x100")

tk.Label(root, text="Top Button!").pack(side=tk.TOP, )

tk.Button(root, text="Hello, Left!").pack(side="left", expand = True, fill = BOTH)
tk.Button(root, text="exit", command = exit).pack(side = tk.TOP, anchor = "e")
tk.Button(root, text="Hello, Right!").pack(side="right", expand = True, fill = BOTH)

tk.Button(
    root,
    text="An option at the bottom!",
).pack(side=tk.BOTTOM)


# Start the event loop.
root.mainloop()

