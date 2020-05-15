from scipy.io import wavfile
from audioop import add
import wave
import contextlib

#currently following along with this work:
#http://andrewslotnick.com/posts/audio-delay-with-python.html

def delay(fileName, mix, feedback, tempo):

    fs, data = wavfile.read(fileName + '.wav', 'r')


    with wave.open(fileName + '.wav','rb') as wave_file:
        params = wave_file.getparams()
        audio_bytes = wave_file.readframes(1000000)

    obj = wave.open(fileName + '_delay.wav', 'wb')
    obj.setnchannels(1)     # sets mono
    obj.setsampwidth(2)     # sets to 16-bits
    obj.setframerate(fs)    # sets sample rate

    offset = params.sampwidth*tempo*int(params.framerate/1000)
    beginning = b'\0'*offset
    end = audio_bytes[:-offset]
    data = add(audio_bytes, beginning+end, params.sampwidth)

    # used to find the length of the wav file
    with contextlib.closing(wave.open(fileName + '.wav', 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)

    for i in range(int(duration * fs)):
        obj.writeframesraw(data)
    obj.close()

