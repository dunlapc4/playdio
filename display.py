import tkinter as tk
from synth import sine, sawtooth
import fileIO


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

        # synthesizer option window
        sineButton = tk.Button(text='Create a synthesizer wave pattern',
                               command=self.create_synth)
        sineButton.pack()


        mergeButton = tk.Button(text='merge audio files',
                               command=self.merge_audio)
        mergeButton.pack()

    def create_synth(self):
        s = tk.Toplevel()
        s.iconbitmap('images/note.ico')
        s.geometry('300x350')
        s.title("synthesizer settings")

        tk.Label(s, text='name').pack()
        name = tk.Entry(s)
        name.pack()

        # duration of clip
        duration = tk.DoubleVar()
        tk.Label(s, text='duration').pack()
        scaleDuration = tk.Scale(s, from_=0.0, to=20.0, variable=duration, orient=tk.HORIZONTAL)
        scaleDuration.pack()

        # sample rate
        fs = tk.DoubleVar()
        tk.Label(s, text='sample rate').pack()
        scaleFs = tk.Scale(s, from_=8000.0, to=48000.0, variable=fs, orient=tk.HORIZONTAL)
        scaleFs.pack()

        # frequency of wave length
        freq = tk.DoubleVar()
        tk.Label(s, text='frequency').pack()
        scaleFreq = tk.Scale(s, from_=20.0, to=1200.0, variable=freq, orient=tk.HORIZONTAL)
        scaleFreq.pack()

        # amplitude of wave
        level = tk.DoubleVar()
        tk.Label(s, text='sound level').pack()
        scaleLevel = tk.Scale(s, from_=0, to=100, variable=level, orient=tk.HORIZONTAL)
        scaleLevel.pack()

        createSine = tk.Button(s, text='create sine wave',
                               command=lambda: sine.sinWav(name.get(),
                               duration.get(), fs.get(), freq.get(),
                               float(level.get()/100.0)))
        createSine.pack()


        createSaw = tk.Button(s, text='create sawtooth wave',
                               command=lambda: sawtooth.sawWav(name.get(), fs.get(), freq.get()))
        createSaw.pack()

    def merge_audio(self):
        m = tk.Toplevel()
        m.iconbitmap('images/note.ico')
        m.geometry('300x350')
        m.title("synthesizer settings")


        tk.Label(m, text='First file name').pack()
        audioA = tk.Entry(m)
        audioA.pack()

        tk.Label(m, text='Second file name').pack()
        audioB = tk.Entry(m)
        audioB.pack()

        blend = tk.Button(m, text='Blend audio sample together',
                              command=lambda: fileIO.blend_audio(audioA.get(), audioB.get()))
        blend.pack()

        link = tk.Button(m, text='link audio samples together in sequence',
                          command=lambda: fileIO.link_audio(audioA.get(), audioB.get()))
        link.pack()


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