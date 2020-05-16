# This is a synthesizer filter for adding sine waves of a given
# duration, sample rate and frequency

import struct
import math
import fileIO

def sinWav(fileName, duration, fs, freq, level):

    maxVol = 32767.0        # max possible volume
    amps = maxVol * level   # Amplitude

    data = bytearray()
    for i in range(int(duration * fs)):
        sample = int(amps * math.sin(freq * math.pi * 2 * float(i) / float(fs)))
        data.extend(struct.pack('<h', sample))

    fileIO.file_output(fileName, fs, data)
