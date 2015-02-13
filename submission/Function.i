%module Function
%{
#include "Function.h"
  %}


%include "std_string.i"
%include "std_vector.i"
%nodefaultctor Function;
%include "Mesh.i"
%include "Solution.i"
%include "SpatialFilter.i"
  
namespace std {
  %template(DoubleVector) vector<double>;
}

using namespace std;

class FunctionPtr {
public:
  Function* operator->();

  %extend {
    FunctionPtr __add__(FunctionPtr f2) {
      return *self + f2;
    }
    FunctionPtr __add__(double value) {
      return *self + value;
    }
    FunctionPtr __radd__(double value) {
      return *self + value;
    }
    FunctionPtr __mul__(double value) {
      return *self * value;
    }
    FunctionPtr __rmul__(double value) {
      return *self * value;
    }
    FunctionPtr __mul__(vector<double> weight) {
      return *self *  weight;
    }
    FunctionPtr __rmul__(vector<double> weight) {
      return *self * weight;
    }
    FunctionPtr __mul__(FunctionPtr f2) {
      return *self * f2;
    }
    FunctionPtr __div__(FunctionPtr scalarDivision) {
      return *self / scalarDivision;
    }
    FunctionPtr __div__(double divisor) {
      return *self / divisor;
    }
    FunctionPtr __rdiv__(double divisor) {
      return divisor / *self;
    }
    FunctionPtr __sub__(FunctionPtr f2) {
      return *self - f2;
    }
    FunctionPtr __sub__(double value) {
      return *self - value;
    }
    FunctionPtr __rsub__(double value) {
      return value - *self;
    }
    FunctionPtr __neg__() {
      return - *self;
    }

    LinearTermPtr __mul__(VarPtr v) {
      return *self * v;
    }

    LinearTermPtr __rmul__(VarPtr v) {
      return *self * v;
    }

  }
};


class Function{
 public:
  FunctionPtr x();
  FunctionPtr y();
  FunctionPtr dx();
  FunctionPtr dy();
  FunctionPtr div();
  FunctionPtr grad();
  int rank();
  double l2norm(MeshPtr mesh, int cubatureDegreeEnrichment = 0);
  std::string displayString();
  double evaluate(double x, double y);
  static FunctionPtr composedFunction( FunctionPtr f, FunctionPtr g);
  static FunctionPtr constant(double value);
  static FunctionPtr vectorize(FunctionPtr f1, FunctionPtr f2);
  static FunctionPtr normal();
  static FunctionPtr solution(VarPtr var, SolutionPtr soln);
  static FunctionPtr xn(int n=1);
  static FunctionPtr yn(int n=1);
  %extend {
     std::string __str__() {
       return self->displayString();
     }
  }

};
