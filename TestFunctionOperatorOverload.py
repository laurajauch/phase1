import Function
import unittest


class TestFunction(unittest.TestCase):
    """Test operator*"""
    def testoperator*(self):
        self.assertalmostequal(6, Function.Function_operator*(Function.Function_constant(2), Function.Function_constant(3)).evaluate(5,-2)), delta=1e-12)
	self.assertalmostequal(30, Function.Function_operator*(10, Function.Function_constant(3)).evaluate(1,200)), delta=1e-12)
	self.assertalmostequal(12, Function.Function_operator*(Function.Function_constant(4), 3).evaluate(-7,20)), delta=1e-12)
	self.assertalmostequal(6, Function.Function_operator*(vector(3,4), Function.Function_xn(1)).evaluate(2,1), delta=1e-12)
	self.assertalmostequal(2, Function.Function_operator*(Function.Function_yn(1), vector(3,1)).evaluate(-1,2), delta=1e-12)

     """Test operator/"""
    def testoperator/(self):
	self.assertalmostequal(-5, Function.Function_operator/(Function.Function_constant(-50), Function.Function_constant(10)).evaluate(4,-123), delta=1e-12)
        self.assertalmostequal(2, Function.Function_operator/(Function.Function_constant(6),3).evaluate(10,-6), delta=1e-12)
        self.assertalmostequal(3, Function.Function_operator/(12, Function.Function_constant(4)).evaluate(0,0), delta=1e-12) 

     """Test operator+"""
    def testoperator+(self):
        self.assertalmostequal(40, Function.Function_operator+(Function.Function_constant(22),Function.Function_constant(18)).evaluate(8,-7), delta=1e-12)
	self.assertalmostequal(32, Function.Function_operator+(Function.Function_constant(16), 16).evaluate(5,4), delta=1e-12)
	self.assertalmostequal(Function.Function_operator+(Function.Function_constant(14), 12).evaluate(1,2), 26, delta=1e-12)
     
     """Test operator-"""
    def testoperator-(self):
        self.assertalmostequal(4, Function.Function_operator-(Function.Function_constant(22),Function.Function_constant(18)).evaluate(2,469), delta=1e-12)
	self.assertalmostequal(-10, Function.Function_operator-(Function.Function_constant(0),-10).evaluate(12,46), delta=1e-12)
	self.assertalmostequal(-1, Function.Function_operator-(-5,Function.Function_constant(-4)).evaluate(8,46), delta=1e-12) 
	self.assertalmostequal(-9, Function.Function_operator-(Function.Function_constant(9)).evaluate(-43,12), delta=1e-12) 


# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
