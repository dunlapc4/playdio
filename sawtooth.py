# This is a synthesizer filter for adding sawtooth wave patterns
# of a given duration and sample rate

# The project might soon need directories that categorize filter types

from scipy import signal
import fileIO
import struct
import math

def sawWav(fileName, duration, fs):

    data = bytearray()
    for i in range(int(duration * fs)):
        saw = signal.sawtooth(2)
        data.extend(struct.pack('<h', int(saw)))
    print(type(saw))
    print(data)

    datas = bytearray()
    for i in range(int(duration * fs)):
        samp = signal.sawtooth(2 * math.pi * 5 * i)
        datas.extend(struct.pack('<h', int(samp)))
    print(datas)

    fileIO.file_output(fileName, fs, datas)
