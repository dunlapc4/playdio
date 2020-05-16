# This is a synthesizer filter for adding sawtooth wave patterns
# of a given duration and sample rate

from scipy import signal
import fileIO
import math
import numpy as np

def sawWav(fileName, fs, freq):

    t = np.linspace(0, 1, int(fs))
    dat = signal.sawtooth(2 * math.pi * freq * t)

    fileIO.file_output(fileName, fs, dat.tobytes())
