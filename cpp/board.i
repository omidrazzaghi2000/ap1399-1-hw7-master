/* File : example.i */
%module board

%{
#include "board.h"
%}

/* Let's just grab the original header file here */
%include "board.h"