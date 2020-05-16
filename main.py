from playsound import playsound
import sawtooth
import sine
import delay

fileName = 'sample'
duration = 1.0          # length in seconds
fs = 48000.0            # sample rate, Hz
freq = 480              # sine freq, Hz, f
level = .25             # percent of volume level

#sine.sinWav(fileName, duration, fs, freq, level)
sawtooth.sawWav(fileName, duration, fs)

mix = .5        # dry & wet ratio of delay effect
feedback = 1    # number of repeats made
tempo = 1000    # time delay in milliseconds
#delay.delay('gc', mix, feedback, tempo)

#playsound('sample' + '.wav')
