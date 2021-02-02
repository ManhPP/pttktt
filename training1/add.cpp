#include <iostream>

using namespace std;

int main(){
    string a, b;

    cin>>a;
    cin>>b;
    int lenA = a.length();
    int lenB = b.length();

    if (lenA > lenB){
        swap(a,b);
        swap(lenA, lenB);
    }

    int offset = lenB - lenA;
    int carry = 0;
    string c = "";

    for (int i = lenA - 1; i >= 0; i--){
        int sum = (a[i] - '0') + (b[i+offset] - '0') + carry;
        c.push_back(sum%10 + '0');
        carry = sum/10;
    }

    if (carry) 
        c.push_back(carry+'0');


    cout << string(c.rbegin(), c.rend());
    return 0;
}   