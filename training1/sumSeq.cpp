#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    unsigned long long int a, r = 0;
    unsigned long long  int mod = 1e9 + 7;
    for (int i = 0; i< n; i++){
        cin >> a;
        r = (r + a%mod)%mod;
    }
    cout<<r;
}