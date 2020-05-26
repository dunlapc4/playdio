import wave
from playsound import playsound


def playTrack(fileName):
    track = 'audioclips/' + fileName
    playsound(track)

