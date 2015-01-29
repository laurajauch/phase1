import SpatialFilter
import unittest

class TestSpatialFilter(unittest.TestCase):
    """Test matchespoint(), intersectionFilter(), negatedFilter(), untionFilter(), allSpace()"""
    def testmatchespoint(self):
        self.assertTrue(SpatialFilter.allSpace()->matchesPoint(1,1))
        self.assertTrue(SpatialFilter.allSpace()->matchesPoint(vector(3,2)))
        self.assertFalse(SpatialFilter.intersectionFilter(SpatialFilter.allSpace(),SpatialFilter.allSpace())->matchesPoint(2,4))
        self.assertFalse(SpatialFilter.negatedFilter(SpatialFilter.allSpace())->matchesPoint(5,8))
        self.assertTrue(SpatialFilter.unionFilter(SpatialFilter.allSpace(),SpatialFilter.allSpace())->matchesPoint(6,1))

    """Test matchingX()"""
    def testmatchingX(self):
        self.assertTrue(SpatialFilter.matchingX(3)->matchesPoint(3,2))
        self.assertFalse(SpatialFilter.matchingX(4)->matchesPoint(1,4))
    """Test matchingY()"""
    def testmatchingY(self):
        self.assertTrue(SpatialFilter.matchingY(2)->matchesPoint(3,2))
        self.assertFalse(SpatialFilter.matchingY(4)->matchesPoint(4,9))

    """Test lessThanX()"""
    def testlessThanX(self):
        self.assertTrue(SpatialFilter.lessThanX(7)->matchesPoint(3,2))
        self.assertFalse(SpatialFilter.lessThanX(8)->matchesPoint(10,9))
    """Test greaterThanX()"""
    def testgreaterThanX(self):
        self.assertTrue(SpatialFilter.greaterThanX(1)->matchesPoint(3,2))
        self.assertFalse(SpatialFilter.greaterThanX(16)->matchesPoint(10,9))
        
    """Test lessThanY()"""
    def testlessThanY():
        self.assertTrue(SpatialFilter.lessThanY(7)->matchesPoint(31,2))
        self.assertFalse(SpatialFilter.lessThanY(8)->matchesPoint(0,9))
    """Test greaterThanY()"""
    def testgreaterThanY():
        self.assertTrue(SpatialFilter.greaterThanY(1)->matchesPoint(1,2))
        self.assertFalse(SpatialFilter.greaterThanY(16)->matchesPoint(103,9))


# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
