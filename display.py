import tkinter as tk
from synth import sine

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

        # sine wave option window
        sineButton = tk.Button(self, text="Create Sine Wave", command=self.sine_window)
        sineButton.grid(row=11, column=1)

    def client_exit(self):
        exit()

    def about_window(self):
        aboutWindow = tk.Toplevel(app)
        w = tk.Label(aboutWindow, text="Playdio 0.1.0")
        w.pack()

    def text_field(self):
        sample = tk.Label(self, text="sample input")
        sample.grid(row=4, column=4)
        sample.pack()

    def sine_window(self):
        sineWindow = tk.Toplevel(app)
        # sample input
        # fields = 'fileName', 'duration', 'fs', 'freq', 'level'
        # fileName = tk.StringVar()
        # duration = tk.DoubleVar()
        # fs       = tk.DoubleVar()
        # freq     = tk.DoubleVar()
        # level    = 1

        tk.Label(sineWindow, text="name").grid(row=6)
        name = tk.Entry(sineWindow)
        name.grid(row=6, column=1)
        fileName = name.get()


        tk.Label(sineWindow, text="duration").grid(row=8)
        length = tk.Entry(self)
        length.grid(row=8, column=1)
        #duration = length.get()

        fs = 48000.0
        freq = 480.0
        level = 1

        duration = 6.0

        submitSine = tk.Button(sineWindow, text="Submit", width=10, command=sine.sinWav(str(fileName), float(duration), float(fs), float(freq), int(level)))
        submitSine.grid(row=9, column=9)





root = tk.Tk()
root.iconbitmap('images/note.ico')
root.geometry('800x500')
app = Window(master = root)

app.mainloop()