import wave
import struct
import math

def sinWav(fileName):

    sampleRate = 48000.0        # Hz, fs
    duration = 1.0              # time in seconds
    freq = 440.0                # sine freq, Hz, f
    maxVol = 32767.0            # Volume
    quarterAmp = maxVol * .25   # Amplitude

    objS = wave.open(fileName + '.wav', 'wb')
    objS.setnchannels(1)  # set mono
    objS.setsampwidth(2)  # set to 16-bits
    objS.setframerate(sampleRate)

    for i in range(int(duration * sampleRate)):
        sample = int(quarterAmp * math.sin(freq * math.pi * 2 * float(i) / float(sampleRate)))
        data = struct.pack('<h', sample)
        objS.writeframesraw(data)

    objS.close()
