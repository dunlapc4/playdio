import unittest
import logging
from synth import sine
import os

#logger = logging.getLogger()
#logger.level = logging.DEBUG


class TestSynth(unittest.TestCase):
    sine.sinWav(fileName='sinTest', duration=1, fs=48000.0, freq=480.0, level=1)

#    def test_sine(self):
#        self.assertTrue(os.path.isfile('audioclips/sinTest.wav'))
