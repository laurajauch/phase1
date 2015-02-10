import BC
import Var
import VarFactory
import SpatialFilter
import Function
import unittest

boundary = BC.BC_bc()
vf = VarFactory.VarFactory();
vtest = vf.test(17);

class TestBC(unittest.TestCase):
    """ test BC()"""
    def testBoundCond(self):
        self.assertFalse(boundary.bcsImposed(1))
        
    def testSinglePoint(self):
        boundary.addSinglePointBC(17, 0.0)    
        self.assertTrue(boundary.singlePointBC(17))
        self.assertFalse(boundary.bcsImposed(17)) 
        self.assertAlmostEqual(boundary.valueForSinglePointBC(17), 0.0, delta = 1e-12)
        self.assertEqual(boundary.vertexForSinglePointBC(17), -1)
        #how test GlobalIndexType?
        
    def testZeroMean(self):
        #boundary.addZeroMeanConstraint(vtest)    
        #self.assertTrue(boundary.imposeZeroMeanConstarint(17))
        #boundary.removeZeroMeanConstraint(vtest)
        #self.assertFalse(boundary.imposeZeroMeanConstraint(varID))
        pass
    
    """addDirichlet, getDirichletBC, getSpatiallyFilteredFunctionForDirichletBC"""    
    def testDirichlet(self):    
        #self.assertTrue(BC.addDirchlet(VarFactory.fluxVar("pizza"),SpatialFilter.lessThanX(12.0), Function.xn(4)).something())
        pass
        
