// https://open.kattis.com/problems/gcdandlcm
// Time: 2022-09-10 17:50:05
// title: GCD and LCM
// language: C++


#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n, m, i=1;
    cin>>n>>m;
    long long gcd = n, lcm = m, g;
    vector<long long> v;
    for(; i*i<n; i++){
        if(n%i == 0){
            v.push_back(i);
            v.push_back(n/i);
        }
    }
    if(i*i == n)v.push_back(i);

    n = m;
    i = 1;
    for(; i*i<n; i++){
        if(n%i == 0){
            v.push_back(i);
            v.push_back(n/i);
        }
    }
    if(i*i == n)v.push_back(i);
    sort(v.begin(), v.end());

    set<pair<long long, long long>>ans;
    for(auto x: v){
        for(auto y: v){
            g = __gcd(x, y);
            if(g == gcd && x/g*y == lcm)ans.insert({x, y});
        }
    }
    for(auto r: ans)cout<<r.first<<" "<<r.second<<endl;


}
