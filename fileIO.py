from scipy.io import wavfile
import wave
import numpy as np

def file_input(fileName):

    fs, data = wavfile.read('audioclips/' + fileName + '.wav', 'r')

    w = wave.open(fileName + '.wav', 'wb')
    w.setnchannels(1)     # sets mono
    w.setsampwidth(2)     # sets to 16-bits
    w.setframerate(fs)    # sets sample rate

    return fs, data, w

def file_output(fileName, fs, data):

    numChan = 1
    w = wave.open('audioclips/' + fileName + '.wav', 'wb')
    w.setnchannels(numChan)   # sets mono
    w.setsampwidth(2)         # sets to 16-bits
    w.setframerate(fs)        # sets sample rate

    bitDepth = 2                # seems to work. Thought it would be 16

    duration = len(data)/(fs * numChan * bitDepth)

    w.writeframesraw(data)
    w.close()


# combines two audio files together as one simultaneous occurrence
def blend_audio(file1, file2):
    # provide from:
    # https://stackoverflow.com/questions/4039158/mixing-two-audio-files-together-with-python

    inFiles =['audioclips/' + file1 + '.wav', 'audioclips/' + file2 + '.wav']
    outFile = 'audioclips/blend.wav'
    wavs = [wave.open(fn) for fn in inFiles]
    frames = [w.readframes(w.getnframes()) for w in wavs]

    # here's efficient numpy conversion of the raw byte buffers
    # '<i2' is a little-endian two-byte integer.
    samples = [np.frombuffer(f, dtype='<i2') for f in frames]   # interpret buffer as 1d arr
    samples = [samp.astype(np.float64) for samp in samples]

    # mix as much as possible
    n = min(map(len, samples))
    mix = samples[0][:n] + samples[1][:n]

    #file_output('mix', 48000.0, mix)


    # Save the result
    out = wave.open(outFile, 'w')
    out.setparams(wavs[0].getparams())

    # before saving, we want to convert back to '<i2' bytes:
    out.writeframes(mix.astype('<i2').tobytes())
    out.close()

def link_audio(file1, file2):
    outFile = 'link'

    w = wave.open('audioclips/' + file1 + '.wav', 'rb')
    data1 = w.readframes(w.getnframes())
    w.close()

    w = wave.open('audioclips/' + file2 + '.wav', 'rb')
    data2 = w.readframes(w.getnframes())
    w.close()

    w = wave.open('audioclips/' + file2 + '.wav', 'rb')
    params = w.getparams()
    w.close()

    out = wave.open('audioclips/' + outFile + '.wav', 'wb')
    out.setparams(params)
    out.writeframes(data1)
    out.writeframes(data2)
    out.close()


