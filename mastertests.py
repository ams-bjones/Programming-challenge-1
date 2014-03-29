import multiples
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        #print (multiples.multiplelist(5,20))
        #print ([5,10,15])
        assert( multiples.multiplelist(5,20)==[5,10,15]) #Test 1 fails
        
    def test2(self):
        inList = [1,2,3]
        total = 6
        assert (multiples.totalList(inList) == total) #test 2 fails
    
    def test3(self):
        inlist = multiples.multiplelist(5,20)
        total = 30
        assert (multiples.totalList(inlist)==total) #test 3 fails

if __name__ == '__main__':
    unittest.main()