from playsound import playsound
import sample

fileName = 'sin'

sample.sinWav(fileName)

playsound(fileName + '.wav')