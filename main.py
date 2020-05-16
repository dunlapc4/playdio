from playsound import playsound
import sawtooth
import sine
import delay

fileName = 'sample'

#sine.sinWav(fileName)
#sawtooth.sawWav(fileName)

mix = .5        # dry & wet ratio of delay effect
feedback = 1    # number of repeats made
tempo = 1000    # time delay in milliseconds
delay.delay('gc', mix, feedback, tempo)

#playsound('sample' + '.wav')
