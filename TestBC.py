import BC
import Var
import VarFactory
import unittest


class TestBC(unittest.TestCase):

    def testBoundCond(self):
        self.assertTrue(BC.bcsImposed(?))



        self.assertTrue(BC.addSinglePointBC(17, 0.0).singlePointBC(17)
        
