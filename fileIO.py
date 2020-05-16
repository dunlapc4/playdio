from scipy.io import wavfile
import wave
import numpy as np

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

def combine_audio(file1, file2):
    # provide from:
    # https://stackoverflow.com/questions/4039158/mixing-two-audio-files-together-with-python

    fnames =['audioclips/' + file1 + '.wav', 'audioclips/' + file2 + '.wav']
    wavs = [wave.open(fn) for fn in fnames]
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
    mix_wav = wave.open('audioclips/mix.wav', 'w')
    mix_wav.setparams(wavs[0].getparams())
    #print(type(mix_wav))

    # before saving, we want to convert back to '<i2' bytes:
    mix_wav.writeframes(mix.astype('<i2').tobytes())
    mix_wav.close()