#include<iostream>
using namespace std; 
  
int main() 
{ 
    string a, b;
    cin >> a;
    cin >> b;
    long long int m = 1e9 + 7;
    unsigned long long int modA =  0, modB = 0;
    
    for (int i = 0; i < a.length(); i++){
        modA = (modA * 10 + (a[i] - '0'))%m;
    }

    for (int i = 0; i < b.length(); i++){
        modB = (modB * 10 + (b[i] - '0'))%(m-1);
    }

    unsigned long long int result = 1; 
    while (modB) { 
        if (modB%2 == 1) 
            result = result * modA % m; 
        modB /= 2; 
        modA = modA * modA % m; 
    } 

    cout << result; 
    return 0; 
} 