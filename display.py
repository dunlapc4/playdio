import tkinter as tk
from tkinter import ttk
from synth import sine, sawtooth
from effect import delay
import fileIO
import player
import os


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
        edit.add_command(label='Create Synthesizer',
                         command=self.create_synth)
        edit.add_command(label='Merge Audio', command=self.merge_audio)
        edit.add_command(label='Create Audio Effect',
                         command=self.create_effect)
        menu.add_cascade(label='Edit', menu=edit)

        # "help" drop-down menu

        help = tk.Menu(menu)
        help.add_command(label='About Playdio...',
                         command=self.about_window)
        menu.add_cascade(label='Help', menu=help)

        tk.Label(text='''





 Welcome to our digital audio effects sandbox!
Feel free to sample what we have so far in the "Edit" Menu option



''').pack()

        tk.Label(text='Select an audio file to play back').pack()
        fileList = os.listdir('audioclips/')
        list = ttk.Combobox(values=fileList)
        list.pack()

        # had to add "label", so that tkinter doesn't memory dump the image

        play = tk.PhotoImage(file='images/play.png')
        label = tk.Label(image=play)
        label.image = play
        play = tk.Button(image=play, command=lambda : \
                         player.playTrack(list.get()))
        play.pack()

    def create_synth(self):
        s = tk.Toplevel()
        s.iconbitmap('images/note.ico')
        s.geometry('300x225')
        s.title('synthesizer settings')

        tk.Label(s, text='Name for audio file:').grid(row=1)
        name = tk.Entry(s)
        name.grid(row=1, column=1)

        # duration of clip

        duration = tk.DoubleVar()
        duration.set(5.0)
        tk.Label(s, text='duration').grid(row=3)
        scaleDuration = tk.Scale(s, from_=0.0, to=20.0,
                                 variable=duration,
                                 orient=tk.HORIZONTAL)
        scaleDuration.grid(row=3, column=1)

        # sample rate

        fs = tk.DoubleVar()
        fs.set(48000.0)
        tk.Label(s, text='sample rate').grid(row=5)
        scaleFs = tk.Scale(s, from_=8000.0, to=48000.0, variable=fs,
                           orient=tk.HORIZONTAL)
        scaleFs.grid(row=5, column=1)

        # frequency of wave length

        freq = tk.DoubleVar()
        freq.set(480)
        tk.Label(s, text='frequency').grid(row=7)
        scaleFreq = tk.Scale(s, from_=20.0, to=1200.0, variable=freq,
                             orient=tk.HORIZONTAL)
        scaleFreq.grid(row=7, column=1)

        # amplitude of wave

        level = tk.DoubleVar()
        level.set(100)
        tk.Label(s, text='sound level').grid(row=9)
        scaleLevel = tk.Scale(s, from_=0, to=100, variable=level,
                              orient=tk.HORIZONTAL)
        scaleLevel.grid(row=9, column=1)

        createSine = tk.Button(s, text='save as sine wave',
                               command=lambda : sine.sinWav(name.get(),
                               duration.get(), fs.get(), freq.get(),
                               float(level.get() / 100.0)))
        createSine.grid(row=12, column=0)

        createSaw = tk.Button(s, text='save as sawtooth wave',
                              command=lambda : \
                              sawtooth.sawWav(name.get(), fs.get(),
                              freq.get()))
        createSaw.grid(row=12, column=1)

    def create_effect(self):
        e = tk.Toplevel()
        e.iconbitmap('images/note.ico')
        e.geometry('300x350')
        e.title('effects settings')

        tk.Label(e, text='Select a file to edit').pack()
        list = os.listdir('audioclips/')
        name = ttk.Combobox(e, values=list)
        name.pack()

        mix = 0
        feedback = 0

        # delay in milliseconds

        tempo = tk.IntVar()
        tempo.set(1000)
        tk.Label(e, text='tempo').pack()
        scaleTempo = tk.Scale(e, from_=0, to=1000, variable=tempo,
                              orient=tk.HORIZONTAL)
        scaleTempo.pack()

        blend = tk.Button(e, text='Blend audio sample together',
                          command=lambda : delay.delay(name.get(), mix,
                          feedback, tempo.get()))
        blend.pack()

    def merge_audio(self):
        m = tk.Toplevel()
        m.iconbitmap('images/note.ico')
        m.geometry('650x100')
        m.title('merge settings')

        tk.Label(m, text='Select two files to be edited together:'
                 ).grid(row=1, column=0)
        audioList = os.listdir('audioclips/')
        listA = ttk.Combobox(m, values=audioList)
        listA.grid(row=1, column=1)
        listB = ttk.Combobox(m, values=audioList)
        listB.grid(row=1, column=2)


        tk.Label(m, text='Name for audio file:').grid(row=3)
        name = tk.Entry(m)
        name.grid(row=3, column=1)


        blend = tk.Button(m, text='Blend audio sample together',
                          command=lambda : \
                          fileIO.blend_audio(listA.get(), listB.get(), name.get()))
        blend.grid(row=4, column=1)

        link = tk.Button(m,
                         text='link audio samples together in sequence'
                         , command=lambda : \
                         fileIO.link_audio(listA.get(), listB.get(), name.get()))
        link.grid(row=4, column=2)

    def client_exit(self):
        exit()

    def about_window(self):
        aboutWindow = tk.Toplevel(app)
        aboutWindow.iconbitmap('images/note.ico')
        aboutWindow.title('About Playdio')
        w = tk.Label(aboutWindow, text='\nPlaydio 0.1.0\n\nDevelopers:\nChristopher Teters\nConor Dunlap')
        w.pack()

    def text_field(self):
        sample = tk.Label(self, text='sample input')
        sample.grid(row=4, column=4)
        sample.pack()


root = tk.Tk()
root.iconbitmap('images/note.ico')
root.geometry('500x300')
app = Window(master=root)

app.mainloop()
