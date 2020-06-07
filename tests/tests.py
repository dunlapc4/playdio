import unittest
#import logging
#from synth import sine
#import os
import sys
sys.path.append('../')
import fileIO.py


 #test
#logger = logging.getLogger()
#logger.level = logging.DEBUG


class TestSynth(unittest.TestCase):
#    sine.sinWav(fileName="sinTest", duration=1, fs=48000.0, freq=480.0, level=1)

    def test_sine(self):
        self.assertTrue(os.path.isfile('audioclips/sinTest.wav'))

    def test_self(self):
        self.assertTrue('True')

    def test_file_input(self):
        file_input("test.py")
        print("test")

    def test_extentsion_check(self):
        self.extentsion_check(fileName)
