#include<iostream>
#include<math.h>
using namespace std;

unsigned long long c = (int)pow(10,9) + 7;

int factorial(int n){
    int fact = 1;
    for (int i = 1; i <=n; ++i) {
        fact *= i;
    }
    return fact;
}

int main(){
    int n, k;
    cin >> n;
    cin >> k;
    cout<< (factorial(n+k-1)/(factorial(n) * factorial(k-1)))%c;
    
    return 0;
}
