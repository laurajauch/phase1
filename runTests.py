from TestSpatialFilter import *
from TestFunction import *
from TestBC import *
import unittest

testSuite = unittest.makeSuite(TestSpatialFilter)
testSuite.addTest(unittest.makeSuite(TestFunction)
testSuite.addTest(unittest.makeSuite(TestBC)

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
