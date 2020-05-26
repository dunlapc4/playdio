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
Feel free to sample what we have so far in the "Edit"



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
        s.geometry('300x350')
        s.title('synthesizer settings')

        tk.Label(s, text='Name for the file to be created').pack()
        name = tk.Entry(s)
        name.pack()

        # duration of clip

        duration = tk.DoubleVar()
        duration.set(5.0)
        tk.Label(s, text='duration').pack()
        scaleDuration = tk.Scale(s, from_=0.0, to=20.0,
                                 variable=duration,
                                 orient=tk.HORIZONTAL)
        scaleDuration.pack()

        # sample rate

        fs = tk.DoubleVar()
        fs.set(48000.0)
        tk.Label(s, text='sample rate').pack()
        scaleFs = tk.Scale(s, from_=8000.0, to=48000.0, variable=fs,
                           orient=tk.HORIZONTAL)
        scaleFs.pack()

        # frequency of wave length

        freq = tk.DoubleVar()
        freq.set(480)
        tk.Label(s, text='frequency').pack()
        scaleFreq = tk.Scale(s, from_=20.0, to=1200.0, variable=freq,
                             orient=tk.HORIZONTAL)
        scaleFreq.pack()

        # amplitude of wave

        level = tk.DoubleVar()
        level.set(100)
        tk.Label(s, text='sound level').pack()
        scaleLevel = tk.Scale(s, from_=0, to=100, variable=level,
                              orient=tk.HORIZONTAL)
        scaleLevel.pack()

        createSine = tk.Button(s, text='create sine wave',
                               command=lambda : sine.sinWav(name.get(),
                               duration.get(), fs.get(), freq.get(),
                               float(level.get() / 100.0)))
        createSine.pack()

        createSaw = tk.Button(s, text='create sawtooth wave',
                              command=lambda : \
                              sawtooth.sawWav(name.get(), fs.get(),
                              freq.get()))
        createSaw.pack()

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
        m.geometry('300x350')
        m.title('merge settings')

        tk.Label(m, text='Select two files to be edited together'
                 ).pack()
        audioList = os.listdir('audioclips/')
        listA = ttk.Combobox(m, values=audioList)
        listA.pack()
        listB = ttk.Combobox(m, values=audioList)
        listB.pack()

        blend = tk.Button(m, text='Blend audio sample together',
                          command=lambda : \
                          fileIO.blend_audio(listA.get(), listB.get()))
        blend.pack()

        link = tk.Button(m,
                         text='link audio samples together in sequence'
                         , command=lambda : \
                         fileIO.link_audio(listA.get(), listB.get()))
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
root.geometry('500x300')
app = Window(master=root)

app.mainloop()
