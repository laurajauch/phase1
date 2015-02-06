import Function
#import Var
#import Solution
#import Mesh
#import MeshFactory
import unittest

x1 = Function.Function_xn(2)
y1 = Function.Function_yn(1)
z = Function.Function_constant(0)

class TestFunction(unittest.TestCase):
    """Test x(), y(), vectorize(), evaluate() """
    

    def testComponent(self):
        self.assertAlmostEqual(4,Function.Function_vectorize(x1, y1).x().evaluate(2,3),delta =1e-12)
        self.assertAlmostEqual(3,Function.Function_vectorize(x1, y1).y().evaluate(2,3),delta =1e-12)
        

    """ Test dx(), dy(), div(), grad()"""
    def testCalc(self):
        self.assertAlmostEqual(0,Function.Function_constant(2).dx().evaluate(1,2),delta=1e-12)
        self.assertAlmostEqual(0,Function.Function_constant(2).dy().evaluate(1,2),delta=1e-12)
        
        # problem?
        #self.assertAlmostEqual(0,Function.Function_constant(9).div().evaluate(1,2),delta=1e-12)
        
        # problem? 
        #self.assertAlmostEqual(0,Function.Function_constant(9).grad().evaluate(1,2),delta=1e-12)

    """ Test rank() """
    def testRank(self):
        self.assertEqual(0, Function.Function_constant(2).rank())
        self.assertEqual(1, Function.Function_vectorize(x1,y1).rank())

    """ Test 12norm() """
    def testNorm(self):
        # Problem
        #self.assertAlmostEqual(Function.l2norm(MeshPtr), 342 ,delta = 1e-12) 
        pass

    """ Test displayString()"""
    def testDisplayString(self):
        self.assertEqual("y",Function.Function_vectorize(y1, z).x().displayString())
        self.assertEqual("(y,0)",Function.Function_vectorize(y1, z).displayString())

    """ Test composedFunction(), constant(), normal(), solution(), xn(), yn() """
    def testEval(self):
        self.assertAlmostEqual(3, Function.Function_xn(1).evaluate(3, 2), delta=1e-12)
        self.assertAlmostEqual(2, Function.Function_yn(1).evaluate(3, 2), delta=1e-12)
        self.assertAlmostEqual(12, Function.Function_constant(12).evaluate(2, 2), delta = 1e-12)
        # Problem?
        #self.assertAlmostEqual(4, Function.Function_composedFunction(y1, x1).evaluate(2, 0),delta=1e-12)
