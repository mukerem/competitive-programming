// https://open.kattis.com/problems/factorialpower
// Time: 2022-09-11 19:42:19
// title: Factorial Power
// language: C++


#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n,m, x, y, c, q;
    cin>>n>>m;
    map<long long, long long>prime;
    while(n%2 == 0){
        prime[2]++;
        n /= 2;
    }
    for(long long i=3; i*i <= n; i += 2){
        while(n%i == 0){
            prime[i]++;
            n /= i;
        }
    }
    if(n>1)prime[n]++;

    map<long long, long long>divide;
    long long k = 99999999999999;
    for(auto u: prime){

        x = u.first;
        y = u.second;
        //cout<<x<<" "<<y<<endl;
        c = 0;
        q = x;
        while(q <= m){
            c += m / q;
            q *= x;
        }
        k = min(k, c/ y );
    }
    cout<<k;

}
