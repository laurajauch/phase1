import BC
import Var
import VarFactory
import SpatialFilter
import Function
import unittest

boundary = BC.BC_bc()
vf = VarFactory.VarFactory();

class TestBC(unittest.TestCase):
    """ test BC()"""
    def testBoundCond(self):
        self.assertFalse(boundary.bcsImposed(1))
        
    def testSinglePoint(self):
        boundary.addSinglePointBC(17, 0.0)    
        self.assertTrue(boundary.singlePointBC(17))
        #self.assertTrue(boundary.bcsImposed(17))
        #self.assertAlmostEqual(BC.valueForSinglePointBC, 0.0, delta = 1e-12)
        #self.assertAlmostEqual(BC.vertexForSinglePointBC(17), -1, delta = 1e-12)
        #pass
        
    def testZeroMean(self):    
        #self.assertTrue(BC.addZeroMeanConstaint(VarPtr Field).imposeZeroMeanConstarint(varID))
        #self.assertFalse(BC.removeZeroMeanConstraint(fieldID).imposeZeroMeanConstraint(varID))
        pass
    
    """addDirichlet, getDirichletBC, getSpatiallyFilteredFunctionForDirichletBC"""    
    def testDirichlet(self):    
        #self.assertTrue(BC.addDirchlet(VarFactory.fluxVar("pizza"),SpatialFilter.lessThanX(12.0), Function.xn(4)).something())
        pass
        
