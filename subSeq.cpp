#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    int inputs[n];

    for (int i = 0; i < n; i++){
        cin >> inputs[i];
    }
    int max = inputs[0];
    for (int i = 1; i < n; i++){
        inputs[i] = inputs[i] >= (inputs[i] + inputs[i-1]) ? inputs[i] : (inputs[i] + inputs[i-1]);
        max = inputs[i] > max ? inputs[i] : max;
    }
    cout<< max;
    return 0;
}