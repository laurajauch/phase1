import Function
import unittest

class TestFunction(unittest.TestCase):
    """Test operator*"""
    def testoperator*(self):
        self.assertalmostequal(6, Function.operator*(Function.constant(2), Function.constant(3))->evaluate(5,-2)), delta=1e-12)
	self.assertalmostequal(30, Function.operator*(10, Function.constant(3))->evaluate(1,200)), delta=1e-12)
	self.assertalmostequal(12, Function.operator*(Function.constant(4), 3)->evaluate(-7,20)), delta=1e-12)
	#test operator*(vector<double> weight, FunctionPtr f)
	#test operator*(FunctionPtr f, vector<double> weight)

     """Test operator/"""
    def testoperator/(self):
	self.assertalmostequal(-5, Function.operator/(Function.constant(-50), Function.constant(10))->evaluate(4,-123), delta=1e-12)
        self.assertalmostequal(2, Function.operator/(Function.constant(6),3)->evaluate(10,-6), delta=1e-12)
        self.assertalmostequal(3, Function.operator/(12, Function.constant(4))->evaluate(0,0), delta=1e-12) 

     """Test operator+"""
    def testoperator+(self):
        self.assertalmostequal(40, Function.operator+(Function.constant(22),Function.constant(18))->evaluate(8,-7), delta=1e-12)
	self.assertalmostequal(32, Function.operator+(Function.constant(16), 16)->evaluate(5,4), delta=1e-12)
	self.assertalmostequal(Function.operator+(Function.constant(14), 12)->evaluate(1,2), 26, delta=1e-12)
     
     """Test operator-"""
    def testoperator-(self):
        self.assertalmostequal(4, Function.operator-(Function.constant(22),Function.constant(18))->evaluate(2,469), delta=1e-12)
	self.assertalmostequal(-10, Function.operator-(Function.constant(0),-10)->evaluate(12,46), delta=1e-12)
	self.assertalmostequal(-1, Function.operator-(-5,Function.constant(-4))->evaluate(8,46), delta=1e-12) 
	self.assertalmostequal(-9, Function.operator-(Function.constant(9))->evaluate(-43,12), delta=1e-12) 


# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
