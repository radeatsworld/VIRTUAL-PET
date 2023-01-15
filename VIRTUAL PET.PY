from tkinter import *
import tkinter as tk
window = tk.Tk()
# WINDOW CONFIG
window.config(highlightbackground='black')
label = tk.Label(window, bd=0, bg='black')
image = tk.PhotoImage(file="C:\\Users\\RAD\\Desktop\\charmander.png")
label.configure(image=image)
window.overrideredirect(True)
window.wm_attributes('-transparentcolor')
label.pack()
window.title('Hello Pet')
window.geometry("300x200+10+20")
window.mainloop()
