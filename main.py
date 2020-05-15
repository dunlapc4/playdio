from playsound import playsound
import sawtooth
import sine

fileName = 'sample'

sine.sinWav(fileName)
sawtooth.sawWav(fileName)

playsound('sample' + '.wav')
