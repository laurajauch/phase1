import Function
import Var
import Solution
import Mesh
import MeshFactory
import unittest

class TestFunction(unittest.TestCase):
    """Test x(), y(), vectorize(), evaluate() """
    def testComponent(self):
        self.assertAlmostEqual(4,Function.Function_vectorize(2x, 3y).x().evaluate(2,3),delta =1e-12)
        self.assertAlmostEqual(9,Function.Function_vectorize(2x, 3y).y().evaluate(2,3),delta =1e-12)
        

    """ Test dx(), dy(), div(), grad()"""
    def testCalc(self):
        self.assertAlmostEqual(0,Function.Function_constant(2).dx().evaluate(1,2),delta=1e-12)
        self.assertAlmostEqual(0,Function.Function_constant(2).dy().evaluate(1,2),delta=1e-12)
        self.assertAlmostEqual(0,Function.Function_constant(9).div().evaluate(1,2),delta=1e-12)
        self.assertAlmostEqual(0,Function.Function_constant(9).grad().evaluate(1,2),delta=1e-12)

    """ Test rank() """
    def testRank(self):
        self.assertEqual(0, Function.Function_constant(2).rank())
        self.assertEqual(1, Function.Function_vectorize(x,y).rank())

    """ Test 12norm() """
    def testNorm(self):
        self.assertAlmostEqual(Function.l2norm(MeshPtr), double ,delta = 1e-12) 

    """ Test displayString()"""
    def testDisplayString(self):
	self.assertEqual("x",Function.Function_vectorize(x, 0).x().displayString())
	self.assertEqual("x",Function.Function_vectorize(x, 0).displayString())

    """ Test composedFunction(), constant(), normal(), solution(), xn(), yn() """
    def testEval(self):
        self.assertAlmostEqual(3, Function.Function_xn(1).evaluate(3, 2), delta=1-e12)
        self.assertAlmostEqual(2, Function.Function_yn(1).evaluate(3, 2), delta=1-e12)
        self.assertAlmostEqual(12, Function.Function_constant(12).evaluate(2, 2), delta = 1e-12)
        self.assertAlmostEqual(12, Function.Function_composedFunction(3y, 2x).evaluate(2, 0),delta=1e-12)
        
