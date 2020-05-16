from scipy import signal
from scipy.io import wavfile
import wave

def sawWav(fileName):

    fs, data = wavfile.read(fileName + '.wav', 'r')
    duration = len(data)/fs

    obj = wave.open(fileName + '_sawtooth.wav', 'wb')
    obj.setnchannels(1)  # set mono
    obj.setsampwidth(2)  # set to 16-bits
    obj.setframerate(fs)

    for i in range(int(duration * fs)):
        saw = signal.sawtooth(2)
        obj.writeframesraw(saw)
    obj.close()
