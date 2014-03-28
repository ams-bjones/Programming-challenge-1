import multiples
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        multiples.multiplelist(5,20)==[5,10,15] #Test 1 fails

if __name__ == '__main__':
    unittest.main()