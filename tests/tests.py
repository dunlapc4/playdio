import unittest
import logging
from synth import sine
import os

logger = logging.getLogger()
logger.level = logging.DEBUG


class TestSynth(unittest.TestCase):

    sinTest = sine.sinWav('sinTest', 1, 48000.0, 480.0, 1)

    def test_sine(self):
        self.assertTrue(os.path.isfile('audioclips/sinTest.wav'))
