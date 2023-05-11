// https://open.kattis.com/problems/fundamentalneighbors
// Time: 2019-11-19 18:49:36
// title: Fundamental Neighbors
// language: C++


#include<bits/stdc++.h>
using namespace std;
#define N 46341
bool p[N];
vector<long long>prime;
void seive()
{
    long long x = sqrt(N);
    p[0]=1;
    p[1]=1;
    for(long long i=2; i<=x; i++)
    {
        if(p[i])continue;
        for(long long j=i+i; j<=N; j+= i)
        {
            p[j]=1;
        }
    }
    for(long long i=2; i<=N; i++)
    {
        if(!p[i])prime.push_back(i);
    }
}

int main()
{
    long long n;
    seive();
    //for(int i=0;i<100;i++)cout<<prime[i]<<" ";
    while(cin>>n)
    {
        long long nn=n;
        map<long long,long long>m;
        while (n!=1)
        {
            bool ch = false;
            for(auto u:prime)
            {
                if(n%u == 0)
                {
                    if(m.count(u) == 0)m[u]=1;
                    else m[u]+= 1;
                    n = n/u;
                    ch = true;
                    break;
                }
            }
            if(!ch)
            {
                m[n]=1;
                n = 1;
            }
        }
        long long ans = 1;
        for(auto u:m){
            ans *= powl(u.second, u.first);
        }
        cout<<nn<<" "<<ans<<endl;

    }
}
