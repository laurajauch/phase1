import BC
#import Var
#import VarFactory
import SpatialFilter
import Function
import unittest

vf = VarFactory.VarFactory_VarFactory()
fv.testVar("test", fs = L2)

class TestBC(unittest.TestCase):
    """ test BC()"""
    def testBoundCond(self):
        #self.assertFalse(BC.BC_bcsImposed(1))
        pass
        
    def testSinglePoint(self):    
        #self.assertTrue(BC.addSinglePointBC(17, 0.0).singlePointBC(17))
        #self.assertTrue(BC.bcsImposed(17))
        #self.assertAlmostEqual(BC.valueForSinglePointBC, 0.0, delta = 1e-12)
        #self.assertAlmostEqual(BC.vertexForSinglePointBC(17), -1, delta = 1e-12)
        pass
        
    def testZeroMean(self):    
        #self.assertTrue(BC.addZeroMeanConstaint(VarPtr Field).imposeZeroMeanConstarint(varID))
        #self.assertFalse(BC.removeZeroMeanConstraint(fieldID).imposeZeroMeanConstraint(varID))
        pass
    
    """addDirichlet, getDirichletBC, getSpatiallyFilteredFunctionForDirichletBC"""    
    def testDirichlet(self):    
        #self.assertTrue(BC.addDirchlet(VarFactory.fluxVar("pizza"),SpatialFilter.lessThanX(12.0), Function.xn(4)).something())
        pass
        
