import Function
import PoissonFormulation
import VarFactory
import Solution
import BF
import Mesh
import MeshFactory
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
        v = Function.Function_vectorize(z , z)
        self.assertAlmostEqual(0.0, v.div().evaluate(1,2), delta = 1e-12)
        self.assertAlmostEqual(2.0, x1.grad().x().evaluate(1,2), delta = 1e-12)

    """ Test rank() """
    def testRank(self):
        self.assertEqual(0, Function.Function_constant(2).rank())
        self.assertEqual(1, Function.Function_vectorize(x1,y1).rank())

    """ Test 12norm() """
    def testNorm(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 1)
        self.assertAlmostEqual(z.l2norm(mesh), 0.0 ,delta = 1e-12) 
        

    """ Test displayString()"""
    def testDisplayString(self):
        self.assertEqual("y",Function.Function_vectorize(y1, z).x().displayString())
        self.assertEqual("(y,0)",Function.Function_vectorize(y1, z).displayString())

    """ Test composedFunction(), constant(), xn(), yn() """
    def testEval(self):
        self.assertAlmostEqual(3, Function.Function_xn(1).evaluate(3, 2), delta=1e-12)
        self.assertAlmostEqual(2, Function.Function_yn(1).evaluate(3, 2), delta=1e-12)
        self.assertAlmostEqual(12, Function.Function_constant(12).evaluate(2, 2), delta = 1e-12)
        x3 = Function.Function_vectorize(z ,z)
        self.assertAlmostEqual(0.0, Function.Function_composedFunction(x1, x3).evaluate(2, 0),delta=1e-12)

    """Test solution()"""
    def testSolution(self):
    	vf = VarFactory.VarFactory();
        p = vf.test(9);
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        pointd = [1.0,1.0]
        pointi = [2,3]
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF, pointd, pointi, 1)
        solution = Solution.Solution_solution(mesh)
        solution.projectOntoMesh(map(p.ID(), z))
        self.assertAlmostEqual(z.l2norm(mesh) , z.solution(p, solution).l2norm(mesh), delta=1e-12)
    	
        #p = VarFactory.fluxVar("Hello")
        #poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        #poissonBF = poissonForm.bf()
        #mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3], 1)
        #solution = Solution.projectOntoMesh(
	#self.assertAlmostEqual(z.l2norm(mesh) , Function.Function_solution(p, Solution.Solution_solution()), 1e-12)
        pass
