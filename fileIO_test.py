import unittest
from fileIO import *



class TestFileIO(unittest.TestCase):


    def test_self(self):
        self.assertTrue('True')

    def test_link_audio(self):
        link_audio("sine.wav", "synth.wav", "test_Link.wav")
        link_audio("sine.wav", "synth.wav", "outcome2.wav")
        with open("audioclips/test_link.wav", "r") as test_read:
            test_audio = test_read.read()
        with open("audioclips/outcome2.wav", "r") as test_read2:
            test_audio_control = test_read2.read()
        self.assertEqual(test_audio_control, test_audio)

    def test_blend_audio(self):
        blend_audio("sine.wav", "synth.wav", "test_blend_output.wav")
        blend_audio("sine.wav", "synth.wav", "output.wav")
        #open files and read contents into strings 
        #then pass strings to the assert_equal
        with open("audioclips/test_blend_output.wav", "r") as myfile:
            testaudio = myfile.read()
        with open("audioclips/output.wav", "r") as myfile2:
            expected = myfile2.read()
        self.assertEqual(testaudio, expected)
        print("test")

