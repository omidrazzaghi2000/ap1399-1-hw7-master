/* File : example.i */
%module traverse

%{
#include "traverse.h"
%}

/* Let's just grab the original header file here */
%include "traverse.h"