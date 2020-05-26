from scipy.io import wavfile
from audioop import add
import wave
import fileIO

#currently following along with this work:
#http://andrewslotnick.com/posts/audio-delay-with-python.html

def delay(fileIn, mix, feedback, tempo, fileOut):

    length = len(fileOut)
    if(fileOut[length - 4] != '.' or fileOut[length - 3] != 'w' or fileOut[length - 2] != 'a' or fileOut[length - 1] != 'v'):
        fileOut = fileOut + '.wav'

    fs, frames = wavfile.read('audioclips/' + fileIn, 'r')

    with wave.open('audioclips/' + fileIn, 'rb') as wave_file:
        params = wave_file.getparams()
        audio_bytes = wave_file.readframes(1000000)

    offset = params.sampwidth*tempo*int(params.framerate/1000)
    beginning = b'\0'*offset
    end = audio_bytes[:-offset]
    data = add(audio_bytes, beginning+end, params.sampwidth)

    fileIO.file_output(fileOut, fs, data)
