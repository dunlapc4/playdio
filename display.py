import tkinter as tk

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("playdio")

        # take allocated space
        self.pack(fill=tk.BOTH, expand=1)

        # creating a menu instance
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # "file" drop-down menu
        file = tk.Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        # "edit" drop-down menu
        edit = tk.Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

        # "help" drop-down menu
        help = tk.Menu(menu)
        help.add_command(label="About Playdio...", command=self.about_window)
        menu.add_cascade(label="Help", menu=help)

    def client_exit(self):
        exit()

    def about_window(self):
        aboutWindow = tk.Toplevel(app)
        w = tk.Label(aboutWindow, text="Playdio 0.1.0")
        w.pack()


root = tk.Tk()
root.geometry('800x500')
app = Window(master = root)
app.mainloop()