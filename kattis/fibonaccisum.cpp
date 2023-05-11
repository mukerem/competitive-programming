// https://open.kattis.com/problems/fibonaccisum
// Time: 2022-09-10 17:20:19
// title: Minimal Fibonacci Sums
// language: C++


#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n, t=0, a=1, b=2, c;
    cin>>n;
    vector<int> v;

    v.push_back(a);
    v.push_back(b);
    t = a+b;
    while(t<=2*n){
        c = a+b;
        v.push_back(c);
        t += c;
        a = b;
        b = c;
    }
    vector<int> ans;
    while(n){
        auto u = upper_bound(v.begin(), v.end(), n);
        u--;
        ans.push_back(*u);
        n -= *u;
    }
    reverse(ans.begin(), ans.end());
    for(auto u: ans)cout<<u<<" ";
}
