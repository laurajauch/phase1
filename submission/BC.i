%module BC
%{
#include "BC.h"
  %}

%include "std_string.i"
%include "std_pair.i"

%nodefaultctor BC;

namespace std {
  %template(PairSpatialFilterFunction) pair<SpatialFilterPtr,FunctionPtr>;
}
using namespace std;

#include "IndexType.h"

typedef unsigned GlobalIndexType;

class BC {
 public:

  #BC();
  static BCPtr bc();
  bool bcsImposed(int varID);
  bool singlePointBC(int varID);
  double valueForSinglePointBC(int varID);
  GlobalIndexType vertexForSinglePointBC(int varID);
  bool imposeZeroMeanConstraint(int varID);
  void addDirichlet(VarPtr traceOrFlux, SpatialFilterPtr spatialPoints, FunctionPtr valueFunction);
  void addSinglePointBC( int fieldID, double value, GlobalIndexType meshVertexNumber = -1 );
  void addZeroMeanConstraint( VarPtr field );
  void removeZeroMeanConstraint( int fieldID );
  pair<SpatialFilterPtr, FunctionPtr> getDirichletBC(int varID);
  FunctionPtr getSpatiallyFilteredFunctionForDirichletBC(int varID);

};

class BCPtr {
public:
	BC* operator->();
};
