import BC
import Var
import VarFactory
import unittest


class TestBC(unittest.TestCase):
        """ test BC()"""
    def testBoundCond(self):
        self.assertFalse(BC.bcsImposed(1))
        
    def testSinglePoint(self):    
        self.assertTrue(BC.addSinglePointBC(17, 0.0).singlePointBC(17))
        self.assertTrue(BC.bcsImposed(17))
        self.assertAlmostEqual(BC.valueForSinglePointBC, 0.0, delta = 1e-12)
        self.assertAlmostEqual(BC.vertexForSinglePointBC(17), -1, delta = 1e-12)
        
    def testZeroMean(self):    
        self.assertTrue(BC.addZeroMeanConstaint(VarPtr Field).imposeZeroMeanConstarint(varID))
        self.assertFalse(BC.removeZeroMeanConstraint(fieldID).imposeZeroMeanConstraint(varID))
        
    def testDirichlet(self):    
        """addDirichlet, getDirichletBC, getSpatiallyFilteredFunctionForDirichletBC"""
        self.assertTrue(BC.addDirchlet(things, , ).something() )
        
