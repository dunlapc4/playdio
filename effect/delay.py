from scipy.io import wavfile
from audioop import add
import wave
import fileIO

#currently following along with this work:
#http://andrewslotnick.com/posts/audio-delay-with-python.html

def delay(fileName, mix, feedback, tempo, fname):

    length = len(fname)
    if(fname[length-4] != '.' or fname[length-3] != 'w' or fname[length-2] != 'a' or fname[length-1] != 'v'):
        fname = fname + '.wav'

    fs, frames = wavfile.read('audioclips/' + fileName, 'r')

    with wave.open('audioclips/' + fileName,'rb') as wave_file:
        params = wave_file.getparams()
        audio_bytes = wave_file.readframes(1000000)

    offset = params.sampwidth*tempo*int(params.framerate/1000)
    beginning = b'\0'*offset
    end = audio_bytes[:-offset]
    data = add(audio_bytes, beginning+end, params.sampwidth)

    fileIO.file_output(fname, fs, data)
