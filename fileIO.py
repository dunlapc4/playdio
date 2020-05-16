from scipy.io import wavfile
import wave

def file_input(fileName):

    fs, data = wavfile.read('audioclips/' + fileName + '.wav', 'r')

    obj = wave.open(fileName + '.wav', 'wb')
    obj.setnchannels(1)     # sets mono
    obj.setsampwidth(2)     # sets to 16-bits
    obj.setframerate(fs)    # sets sample rate

    return fs, data, obj

def file_output(fileName, fs, data):

    numChan = 1
    obj = wave.open('audioclips/' + fileName + '.wav', 'wb')
    obj.setnchannels(numChan)   # sets mono
    obj.setsampwidth(2)         # sets to 16-bits
    obj.setframerate(fs)        # sets sample rate

    bitDepth = 2                # seems to work. Thought it would be 16

    duration = len(data)/(fs * numChan * bitDepth)

    obj.writeframesraw(data)
    obj.close()

