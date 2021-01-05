/* File : example.i */
%module board

%{
#include "board.h"
%}
%include "std_vector.i"
namespace std {
   %template(IntVector) vector<int>;
   %template(VectorOfVectorofInt) vector<vector<int>>;
}
/* Let's just grab the original header file here */
%include "board.h"