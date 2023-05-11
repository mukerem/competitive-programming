// https://open.kattis.com/problems/vectorfunctions
// Time: 2022-09-09 18:15:34
// title: Vector Functions
// language: C++


#include<bits/stdc++.h>
#include "vectorfunctions.h"

void backwards(std::vector<int>& vec){
    reverse(vec.begin(), vec.end());
}
vector<int> everyOther(const vector<int>& vec){
vector<int> v;
    for(int i=0; i<vec.size(); i+=2)
         v.push_back(vec[i]);
return v;
    
}

int smallest(const std::vector<int>& vec){
    return *min_element(vec.begin(), vec.end());
}

int sum(const std::vector<int>& vec){
    return accumulate(vec.begin(), vec.end(), 0);
}

int veryOdd(const std::vector<int>& suchVector){
    int c = 0;
    for(int i=1; i<suchVector.size(); i+=2)if(suchVector[i]%2)c++;
    return c;
}
