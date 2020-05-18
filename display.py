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
        #sineWindow = tk.Toplevel(master=self)

        sineButton = tk.Button(text='Create a sine Wave',
                               command=self.create_sin)
        sineButton.pack()

    def create_sin(self):
        sin = tk.Toplevel()
        sin.iconbitmap('images/note.ico')
        sin.geometry('300x350')
        sin.title("sine settings")

        tk.Label(sin, text='name').pack()
        name = tk.Entry(sin)
        name.pack()

        # duration of clip
        duration = tk.DoubleVar()
        tk.Label(sin, text='duration').pack()
        scaleDuration = tk.Scale(sin, from_=0.0, to=20.0, variable=duration, orient=tk.HORIZONTAL)
        scaleDuration.pack()

        # sample rate
        fs = tk.DoubleVar()
        tk.Label(sin, text='sample rate').pack()
        scaleFs = tk.Scale(sin, from_=8000.0, to=48000.0, variable=fs, orient=tk.HORIZONTAL)
        scaleFs.pack()

        # frequency of wave length
        freq = tk.DoubleVar()
        tk.Label(sin, text='frequency').pack()
        scaleFreq = tk.Scale(sin, from_=20.0, to=1200.0, variable=freq, orient=tk.HORIZONTAL)
        scaleFreq.pack()

        # amplitude of wave
        level = tk.DoubleVar()
        tk.Label(sin, text='sound level').pack()
        scaleLevel = tk.Scale(sin, from_=0, to=100, variable=level, orient=tk.HORIZONTAL)
        scaleLevel.pack()

        submitSine = tk.Button(sin, text='Submit',
                               command=sine.sinWav(name.get(),
                               duration.get(), fs.get(), freq.get(),
                               level.get()))
        submitSine.pack()


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

root = tk.Tk()
root.iconbitmap('images/note.ico')
root.geometry('800x500')
app = Window(master=root)

app.mainloop()