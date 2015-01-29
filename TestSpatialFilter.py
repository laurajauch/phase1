import SpatialFilter
import unittest

class TestSpatialFilter(unittest.TestCase):
    """Test matchespoint(), intersectionFilter(), negatedFilter(), untionFilter(), allSpace()"""
    def testmatchespoint(self):
        self.assertTrue(allSpace().matchesPoint(1,1))
        self.assertTrue(allSpace().matchesPoint(vector(3,2)))
        self.assertFalse(intersectionFilter(allSpace(),allSpace()).matchesPoint(2,4))
        self.assertFalse(negatedFilter(allSpace()).matchesPoint(5,8))
        self.assertTrue(unionFilter(allSpace(),allSpace()).matchesPoint(6,1))

    """Test matchingX()"""
    def testmatchingX(self):
        self.assertTrue(matchingX(3).matchesPoint(3,2))
        self.assertFalse(matchingX(4).matchesPoint(1,4))
    """Test matchingY()"""
    def testmatchingY(self):
        self.assertTrue(matchingY(2).matchesPoint(3,2))
        self.assertFalse(matchingY(4).matchesPoint(4,9))

    """Test lessThanX()"""
    def testlessThanX(self):
        self.assertTrue(lessThanX(7).matchesPoint(3,2))
        self.assertFalse(lessThanX(8).matchesPoint(10,9))
    """Test greaterThanX()"""
    def testgreaterThanX(self):
        self.assertTrue(greaterThanX(1).matchesPoint(3,2))
        self.assertFalse(greaterThanX(16).matchesPoint(10,9))
        
    """Test lessThanY()"""
    def testlessThanY():
        self.assertTrue(lessThanY(7).matchesPoint(31,2))
        self.assertFalse(lessThanY(8).matchesPoint(0,9))
    """Test greaterThanY()"""
    def testgreaterThanY():
        self.assertTrue(greaterThanY(1).matchesPoint(1,2))
        self.assertFalse(greaterThanY(16).matchesPoint(103,9))


# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
