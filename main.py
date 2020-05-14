from playsound import playsound
import sample
import sawtooth

fileName = 'sample'

sawtooth.sawWav(fileName)

playsound(fileName + '.wav')