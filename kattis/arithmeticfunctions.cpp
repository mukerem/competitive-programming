// https://open.kattis.com/problems/arithmeticfunctions
// Time: 2022-08-15 21:49:57
// title: Arithmetic Functions
// language: C++


#include "arithmeticfunctions.h"

// Compute x^3
int cube(int x){
    return x*x*x;
}

// Compute the maximum of x and y
int max(int x, int y){
    int z = x>y?x:y;
    return z;
}

// Compute x - y
int difference(int x, int y){
    return x-y;
}