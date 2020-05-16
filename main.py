from effect import delay
from synth import sine, sawtooth
import fileIO

fileName = 'sample'
audioTest = 'gc'
duration = 5.0          # length in seconds
fs = 48000.0            # sample rate, Hz
freq = 480              # sine freq, Hz, f
level = .25             # percent of volume level

sine.sinWav(fileName, duration, fs, freq, level)
#sawtooth.sawWav(fileName, fs, freq)
fileIO.combine_audio(fileName, audioTest)


mix = .5        # dry & wet ratio of delay effect
feedback = 1    # number of repeats made
tempo = 1000    # time delay in milliseconds
#delay.delay('gc', mix, feedback, tempo)

#playsound('sample' + '.wav')
