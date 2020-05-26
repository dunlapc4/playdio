import tkinter as tk
import display

root = tk.Tk()
root.iconbitmap('images/note.ico')
root.geometry('500x300')
app = display.Window(master=root)

app.mainloop()