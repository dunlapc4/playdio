import wave
import struct
import math
import fileIO

def sinWav(fileName):

    fs = 48000.0                # Hz, sample rate
    duration = 1.0              # time in seconds
    freq = 440.0                # sine freq, Hz, f
    maxVol = 32767.0            # Volume
    quarterAmp = maxVol * .25   # Amplitude

    frame = bytearray()
    for i in range(int(duration * fs)):
        sample = int(quarterAmp * math.sin(freq * math.pi * 2 * float(i) / float(fs)))
        data = struct.pack('<h', sample)
        frame.append('<h', sample)
        print(type(data))


    fileIO.file_output(fileName, fs, data)

