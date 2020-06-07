import unittest
from fileIO import *



class TestFileIO(unittest.TestCase):


    def test_self(self):
        self.assertTrue('True')

    def test_blend_audio(self):
        blend_audio("sine.wav", "synth.wav", "test_blend_output.wav")
        #open files and read contents into strings 
        #then pass strings to the assert_equal
        with open("audioclips/test_blend_output.wav", "r") as myfile:
            testaudio = myfile.read()
        with open("audioclips/outcome2.wav", "r") as myfile2:
            expected = myfile2.read()
        self.assertEqual(testaudio, expected)
        print("test")

