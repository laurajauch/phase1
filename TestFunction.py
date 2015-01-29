import Function
import unittest

class TestFunction(unittest.TestCase):
    """Test x(), y() """
    def testComponent(self):
        self.assertAlmostEqual(4,Function.vectorize(2x, 3y)->x()->evaluate(2,3),delta =1e-12 )
        self.assertAlmostEqual(9,Function.vectorize(2x, 3y)->y()->evaluate(2,3),delta =1e-12 )
        

    """ Test dx(), dy(), div(), grad()"""
    def testCalc(self):
        self.assertAlmostEqual(0,Function.constant(2)->dx()->evaluate(1,2),delta=1e-12)
        self.assertAlmostEqual(0,Function.constant(2)->dy()->evaluate(1,2),delta=1e-12)

        self.assertEqual(0, Function.constant(2)->rank())
        self.assertEqual(1, Function.vectorize(x,y)->rank())
    """ Test displayString()"""
    def testDisplayString(self):
	self.assertEqual("x",Function.vectorize(x, 0)->displayString())

    """ Test evaluate(),composedFunction(), constant(), vectorize(), normal(), solution() """
    def testEval(self):
        self.assertAlmostEqual(3, Function.xn(1)->evaluate(3, 2), delta=1-e12)
        self.assertAlmostEqual(2, Function.yn(1)->evaluate(3, 2), delta=1-e12)
        self.assertAlmostEqual(12, Function.constant(12)->evaluate(2, 2), delta = 1e-12)
        
