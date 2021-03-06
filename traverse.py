# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_traverse', [dirname(__file__)])
        except ImportError:
            import _traverse
            return _traverse
        if fp is not None:
            try:
                _mod = imp.load_module('_traverse', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _traverse = swig_import_helper()
    del swig_import_helper
else:
    import _traverse
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _traverse.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _traverse.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _traverse.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _traverse.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _traverse.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _traverse.SwigPyIterator_equal(self, x)

    def copy(self):
        return _traverse.SwigPyIterator_copy(self)

    def next(self):
        return _traverse.SwigPyIterator_next(self)

    def __next__(self):
        return _traverse.SwigPyIterator___next__(self)

    def previous(self):
        return _traverse.SwigPyIterator_previous(self)

    def advance(self, n):
        return _traverse.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _traverse.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _traverse.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _traverse.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _traverse.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _traverse.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _traverse.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _traverse.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _traverse.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _traverse.IntVector___nonzero__(self)

    def __bool__(self):
        return _traverse.IntVector___bool__(self)

    def __len__(self):
        return _traverse.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _traverse.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _traverse.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _traverse.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _traverse.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _traverse.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _traverse.IntVector___setitem__(self, *args)

    def pop(self):
        return _traverse.IntVector_pop(self)

    def append(self, x):
        return _traverse.IntVector_append(self, x)

    def empty(self):
        return _traverse.IntVector_empty(self)

    def size(self):
        return _traverse.IntVector_size(self)

    def swap(self, v):
        return _traverse.IntVector_swap(self, v)

    def begin(self):
        return _traverse.IntVector_begin(self)

    def end(self):
        return _traverse.IntVector_end(self)

    def rbegin(self):
        return _traverse.IntVector_rbegin(self)

    def rend(self):
        return _traverse.IntVector_rend(self)

    def clear(self):
        return _traverse.IntVector_clear(self)

    def get_allocator(self):
        return _traverse.IntVector_get_allocator(self)

    def pop_back(self):
        return _traverse.IntVector_pop_back(self)

    def erase(self, *args):
        return _traverse.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _traverse.new_IntVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _traverse.IntVector_push_back(self, x)

    def front(self):
        return _traverse.IntVector_front(self)

    def back(self):
        return _traverse.IntVector_back(self)

    def assign(self, n, x):
        return _traverse.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _traverse.IntVector_resize(self, *args)

    def insert(self, *args):
        return _traverse.IntVector_insert(self, *args)

    def reserve(self, n):
        return _traverse.IntVector_reserve(self, n)

    def capacity(self):
        return _traverse.IntVector_capacity(self)
    __swig_destroy__ = _traverse.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _traverse.IntVector_swigregister
IntVector_swigregister(IntVector)


def BFSTraverse(start, goal, numberOfLevel):
    return _traverse.BFSTraverse(start, goal, numberOfLevel)
BFSTraverse = _traverse.BFSTraverse
class DFSTraverseClass(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DFSTraverseClass, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DFSTraverseClass, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _traverse.new_DFSTraverseClass()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _traverse.delete_DFSTraverseClass
    __del__ = lambda self: None

    def DFSTraverse(self, *args):
        return _traverse.DFSTraverseClass_DFSTraverse(self, *args)
DFSTraverseClass_swigregister = _traverse.DFSTraverseClass_swigregister
DFSTraverseClass_swigregister(DFSTraverseClass)

class Node(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Node, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Node, name)
    __repr__ = _swig_repr
    __swig_setmethods__["fatherPointer"] = _traverse.Node_fatherPointer_set
    __swig_getmethods__["fatherPointer"] = _traverse.Node_fatherPointer_get
    if _newclass:
        fatherPointer = _swig_property(_traverse.Node_fatherPointer_get, _traverse.Node_fatherPointer_set)
    __swig_setmethods__["UPchildPointer"] = _traverse.Node_UPchildPointer_set
    __swig_getmethods__["UPchildPointer"] = _traverse.Node_UPchildPointer_get
    if _newclass:
        UPchildPointer = _swig_property(_traverse.Node_UPchildPointer_get, _traverse.Node_UPchildPointer_set)
    __swig_setmethods__["DOWNchildPointer"] = _traverse.Node_DOWNchildPointer_set
    __swig_getmethods__["DOWNchildPointer"] = _traverse.Node_DOWNchildPointer_get
    if _newclass:
        DOWNchildPointer = _swig_property(_traverse.Node_DOWNchildPointer_get, _traverse.Node_DOWNchildPointer_set)
    __swig_setmethods__["LEFTchildPointer"] = _traverse.Node_LEFTchildPointer_set
    __swig_getmethods__["LEFTchildPointer"] = _traverse.Node_LEFTchildPointer_get
    if _newclass:
        LEFTchildPointer = _swig_property(_traverse.Node_LEFTchildPointer_get, _traverse.Node_LEFTchildPointer_set)
    __swig_setmethods__["RIGHTchildPointer"] = _traverse.Node_RIGHTchildPointer_set
    __swig_getmethods__["RIGHTchildPointer"] = _traverse.Node_RIGHTchildPointer_get
    if _newclass:
        RIGHTchildPointer = _swig_property(_traverse.Node_RIGHTchildPointer_get, _traverse.Node_RIGHTchildPointer_set)
    __swig_setmethods__["table"] = _traverse.Node_table_set
    __swig_getmethods__["table"] = _traverse.Node_table_get
    if _newclass:
        table = _swig_property(_traverse.Node_table_get, _traverse.Node_table_set)

    def __init__(self, *args):
        this = _traverse.new_Node(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _traverse.delete_Node
    __del__ = lambda self: None

    def disp(self):
        return _traverse.Node_disp(self)
Node_swigregister = _traverse.Node_swigregister
Node_swigregister(Node)

# This file is compatible with both classic and new-style classes.


