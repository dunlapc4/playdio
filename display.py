import tkinter as tk
from tkinter import ttk
from synth import sine, sawtooth
from effect import delay
import fileIO
import player
import os
import math
import struct
import simpleaudio as sa


def chord(MIDI):

    fs = 48000.0
    duration = .25
    maxVol = 32767.0
    amplitude = maxVol * (1/6)
    freq = 440.0

    note = math.pow(2,(MIDI-69)/12)*freq

    data = bytearray()
    for i in range(int(duration * fs)):
        sample = int(amplitude * math.sin(note * math.pi * 2 * float(i) / float(fs)))
        data.extend(struct.pack('<h', sample))

    play_obj = sa.play_buffer(data, 1, 2, 48000)
    play_obj.wait_done()




class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.keyboard()

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
Feel free to sample what we have so far in the "Edit" options menu



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


        tk.Label(e, text='Name for audio file:').pack()
        fname = tk.Entry(e)
        fname.pack()

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
                          feedback, tempo.get(), fname.get()))
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
        aboutWindow = tk.Toplevel(self)
        aboutWindow.iconbitmap('images/note.ico')
        aboutWindow.title('About Playdio')
        w = tk.Label(aboutWindow, text='\nPlaydio 0.1.0\n\nDevelopers:\nChristopher Teters\nConor Dunlap')
        w.pack()

    def text_field(self):
        sample = tk.Label(self, text='sample input')
        sample.grid(row=4, column=4)
        sample.pack()


    def keyboard(self):
        self.master.title('keyboard')

        C = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(72))
        C.place(relx=0.00)
        D = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(74))
        D.place(relx=0.066)
        E = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(76))
        E.place(relx=0.132)
        F = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(77))
        F.place(relx=0.198)
        G = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(79))
        G.place(relx=0.264)
        A = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(81))
        A.place(relx=0.33)
        B = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(83))
        B.place(relx=0.396)
        C = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(84))
        C.place(relx=0.462)
        D = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(86))
        D.place(relx=0.528)
        E = tk.Button(bg='white',  height = 11, width = 5,command=lambda : chord(88))
        E.place(relx=0.594)
        F = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(89))
        F.place(relx=0.66)
        G = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(91))
        G.place(relx=0.726)
        A = tk.Button(bg='white',  height = 11, width = 5,command=lambda : chord(93))
        A.place(relx=0.792)
        B = tk.Button(bg='white', height = 11, width = 5, command=lambda : chord(95))
        B.place(relx=0.858)
        C = tk.Button(bg='white',  height = 11, width = 5,command=lambda : chord(96))
        C.place(relx=0.924)
        C = tk.Button(text='C#', bg='black', height = 7, width = 3, command=lambda : chord(73))
        C.place(relx=0.033)
        D = tk.Button(text='D#', bg='black', height = 7, width = 3, command=lambda : chord(75))
        D.place(relx=0.099)
        F = tk.Button(text='F#', bg='black', height = 7, width = 3, command=lambda : chord(78))
        F.place(relx=0.231)
        G = tk.Button(text='G#', bg='black', height = 7, width = 3, command=lambda : chord(80))
        G.place(relx=0.297)
        A = tk.Button(text='A#', bg='black', height = 7, width = 3, command=lambda : chord(82))
        A.place(relx=0.363)
        C = tk.Button(text='C#', bg='black', height = 7, width = 3, command=lambda : chord(85))
        C.place(relx=0.495)
        D = tk.Button(text='D#', bg='black',  height = 7, width = 3,command=lambda : chord(87))
        D.place(relx=0.561)
        F = tk.Button(text='F#', bg='black', height = 7, width = 3, command=lambda : chord(90))
        F.place(relx=0.693)
        G = tk.Button(text='G#', bg='black', height = 7, width = 3, command=lambda : chord(92))
        G.place(relx=0.759)
        A = tk.Button(text='A#', bg='black', height = 7, width = 3, command=lambda : chord(94))
        A.place(relx=0.825)