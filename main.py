import tkinter as tk
import display

root = tk.Tk()
root.iconbitmap('images/note.ico')
root.geometry('700x400')
app = display.Window(master=root)

app.mainloop()