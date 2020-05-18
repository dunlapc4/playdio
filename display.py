import tkinter as tk
from synth import sine


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('playdio')

        # take allocated space

        self.pack(fill=tk.BOTH, expand=1)

        # creating a menu instance

        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # "file" drop-down menu

        file = tk.Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # "edit" drop-down menu

        edit = tk.Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

        # "help" drop-down menu

        help = tk.Menu(menu)
        help.add_command(label='About Playdio...',
                         command=self.about_window)
        menu.add_cascade(label='Help', menu=help)

        # sine wave option window

        sineButton = tk.Button(self, text='Create Sine Wave',
                               command=self.sine_window)
        sineButton.grid(row=11, column=1)

    def client_exit(self):
        exit()

    def about_window(self):
        aboutWindow = tk.Toplevel(app)
        w = tk.Label(aboutWindow, text='Playdio 0.1.0')
        w.pack()

    def text_field(self):
        sample = tk.Label(self, text='sample input')
        sample.grid(row=4, column=4)
        sample.pack()


    def sine_window(self):

        def submit_sine():
            sine.sinWav(name.get(),
                        duration.get(), fs.get(), freq.get(),
                        level.get())

        sineWindow = tk.Toplevel(app)

        tk.Label(sineWindow, text='name').pack()
        name = tk.Entry(sineWindow)
        name.pack()

        duration = tk.DoubleVar()
        tk.Label(sineWindow, text='duration').pack()
        scaleDuration = tk.Scale(sineWindow, from_=0.0, to=20.0, variable=duration, orient=tk.HORIZONTAL)
        scaleDuration.pack()


        fs = tk.DoubleVar()
        tk.Label(sineWindow, text='sample rate').pack()
        scaleFs = tk.Scale(sineWindow, from_=8000.0, to=48000.0, variable=fs, orient=tk.HORIZONTAL)
        scaleFs.pack()


        freq = tk.DoubleVar()
        tk.Label(sineWindow, text='frequency').pack()
        scaleFreq = tk.Scale(sineWindow, from_=20.0, to=1200.0, variable=freq, orient=tk.HORIZONTAL)
        scaleFreq.pack()

        level = tk.DoubleVar()
        tk.Label(sineWindow, text='sound level').pack()
        scaleLevel = tk.Scale(sineWindow, from_=0, to=100, variable=level, orient=tk.HORIZONTAL)
        scaleLevel.pack()

        submitSine = tk.Button(sineWindow, text='Submit',
                               command=self.submit_sine).pack()
        submitSine.pack()


root = tk.Tk()
root.iconbitmap('images/note.ico')
root.geometry('800x500')
app = Window(master=root)

app.mainloop()