// https://open.kattis.com/problems/primality
// Time: 2022-09-06 17:12:08
// title: Primality
// language: C++


#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n;
    cin>>n;
    if(n>2 && n%2 == 0){
        cout<<"NO";
        return 0;
    }
    for(long long i = 3; i*i <= n; i+=2){
        if(n%i == 0){
        cout<<"NO";
        return 0;
    }
    }
    cout<<"YES";
    return 0;
}

