#include<iostream>
using namespace std;

void gen(int n, int arr[], int i){
    if (i==n){
        for (int j=0; j < n; j++){
            cout<<arr[j];
        }
        cout<<endl;
        return;
    }

    arr[i] = 0;
    gen(n, arr, i+1);

    arr[i] = 1;
    gen(n, arr, i+1);
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    gen(n, arr, 0);
}