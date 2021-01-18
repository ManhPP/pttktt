#include<iostream>
#include<math.h>
using namespace std;

int main(){
    unsigned long long int a, b;
    cin >> a;
    cin >> b;
    unsigned long long c = (int)pow(10,9) + 7;
    cout << ((a%c)+(b%c))%c;
}