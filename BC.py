# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_BC', [dirname(__file__)])
        except ImportError:
            import _BC
            return _BC
        if fp is not None:
            try:
                _mod = imp.load_module('_BC', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _BC = swig_import_helper()
    del swig_import_helper
else:
    import _BC
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class PairSpatialFilterFunction(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PairSpatialFilterFunction, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PairSpatialFilterFunction, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _BC.new_PairSpatialFilterFunction(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _BC.PairSpatialFilterFunction_first_set
    __swig_getmethods__["first"] = _BC.PairSpatialFilterFunction_first_get
    if _newclass:first = _swig_property(_BC.PairSpatialFilterFunction_first_get, _BC.PairSpatialFilterFunction_first_set)
    __swig_setmethods__["second"] = _BC.PairSpatialFilterFunction_second_set
    __swig_getmethods__["second"] = _BC.PairSpatialFilterFunction_second_get
    if _newclass:second = _swig_property(_BC.PairSpatialFilterFunction_second_get, _BC.PairSpatialFilterFunction_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _BC.delete_PairSpatialFilterFunction
    __del__ = lambda self : None;
PairSpatialFilterFunction_swigregister = _BC.PairSpatialFilterFunction_swigregister
PairSpatialFilterFunction_swigregister(PairSpatialFilterFunction)

class BC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BC, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["bc"] = lambda x: _BC.BC_bc
    if _newclass:bc = staticmethod(_BC.BC_bc)
    def bcsImposed(self, *args): return _BC.BC_bcsImposed(self, *args)
    def singlePointBC(self, *args): return _BC.BC_singlePointBC(self, *args)
    def valueForSinglePointBC(self, *args): return _BC.BC_valueForSinglePointBC(self, *args)
    def vertexForSinglePointBC(self, *args): return _BC.BC_vertexForSinglePointBC(self, *args)
    def imposeZeroMeanConstraint(self, *args): return _BC.BC_imposeZeroMeanConstraint(self, *args)
    def addDirichlet(self, *args): return _BC.BC_addDirichlet(self, *args)
    def addSinglePointBC(self, *args): return _BC.BC_addSinglePointBC(self, *args)
    def addZeroMeanConstraint(self, *args): return _BC.BC_addZeroMeanConstraint(self, *args)
    def removeZeroMeanConstraint(self, *args): return _BC.BC_removeZeroMeanConstraint(self, *args)
    def getDirichletBC(self, *args): return _BC.BC_getDirichletBC(self, *args)
    def getSpatiallyFilteredFunctionForDirichletBC(self, *args): return _BC.BC_getSpatiallyFilteredFunctionForDirichletBC(self, *args)
    __swig_destroy__ = _BC.delete_BC
    __del__ = lambda self : None;
BC_swigregister = _BC.BC_swigregister
BC_swigregister(BC)

def BC_bc():
  return _BC.BC_bc()
BC_bc = _BC.BC_bc

class BCPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BCPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BCPtr, name)
    __repr__ = _swig_repr
    def __deref__(self): return _BC.BCPtr___deref__(self)
    def __init__(self): 
        this = _BC.new_BCPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _BC.delete_BCPtr
    __del__ = lambda self : None;
    def bc(self): return _BC.BCPtr_bc(self)
    def bcsImposed(self, *args): return _BC.BCPtr_bcsImposed(self, *args)
    def singlePointBC(self, *args): return _BC.BCPtr_singlePointBC(self, *args)
    def valueForSinglePointBC(self, *args): return _BC.BCPtr_valueForSinglePointBC(self, *args)
    def vertexForSinglePointBC(self, *args): return _BC.BCPtr_vertexForSinglePointBC(self, *args)
    def imposeZeroMeanConstraint(self, *args): return _BC.BCPtr_imposeZeroMeanConstraint(self, *args)
    def addDirichlet(self, *args): return _BC.BCPtr_addDirichlet(self, *args)
    def addSinglePointBC(self, *args): return _BC.BCPtr_addSinglePointBC(self, *args)
    def addZeroMeanConstraint(self, *args): return _BC.BCPtr_addZeroMeanConstraint(self, *args)
    def removeZeroMeanConstraint(self, *args): return _BC.BCPtr_removeZeroMeanConstraint(self, *args)
    def getDirichletBC(self, *args): return _BC.BCPtr_getDirichletBC(self, *args)
    def getSpatiallyFilteredFunctionForDirichletBC(self, *args): return _BC.BCPtr_getSpatiallyFilteredFunctionForDirichletBC(self, *args)
BCPtr_swigregister = _BC.BCPtr_swigregister
BCPtr_swigregister(BCPtr)

# This file is compatible with both classic and new-style classes.


