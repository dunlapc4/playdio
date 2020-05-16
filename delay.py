from scipy.io import wavfile
from audioop import add
import wave
import fileIO

#currently following along with this work:
#http://andrewslotnick.com/posts/audio-delay-with-python.html

def delay(fileName, mix, feedback, tempo):

    fs, frames = wavfile.read(fileName + '.wav', 'r')

    with wave.open(fileName + '.wav','rb') as wave_file:
        params = wave_file.getparams()
        audio_bytes = wave_file.readframes(1000000)

    offset = params.sampwidth*tempo*int(params.framerate/1000)
    beginning = b'\0'*offset
    end = audio_bytes[:-offset]
    data = add(audio_bytes, beginning+end, params.sampwidth)

    print(type(data))
    print(data)

    fileIO.file_output('delay', fs, data)
