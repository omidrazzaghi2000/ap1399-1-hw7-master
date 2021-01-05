%module traverse
%{
#include "traverse.h"
#include "board.h"
%}

%include "std_vector.i"

// Instantiate templates used by example
namespace std {
   %template(IntVector) vector<Board>;
}

// Include the header file with above prototypes
%include "traverse.h"