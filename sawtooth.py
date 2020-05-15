from scipy import signal
from scipy.io import wavfile
import contextlib
import wave

def sawWav(fileName):

    fs, data = wavfile.read(fileName + '.wav', 'r')

    # used to find the length of the wav file
    with contextlib.closing(wave.open(fileName + '.wav', 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    print("duration: ", duration)

    obj = wave.open(fileName + '_sawtooth.wav', 'wb')
    obj.setnchannels(1)  # set mono
    obj.setsampwidth(2)  # set to 16-bits
    obj.setframerate(fs)

    for i in range(int(duration * fs)):
        saw = signal.sawtooth(2)
        obj.writeframesraw(saw)
    obj.close()
