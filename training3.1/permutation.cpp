#include<iostream>
using namespace std;

void gen(int n, int arr[], int l, int r){
    if (l==r){
        for (int j=0; j < n; j++){
            cout<<arr[j]<< " ";
        }
        cout<<endl;
        return;
    }

    for (int i = l; i <= r; i++){
        swap(arr[l], arr[i]);
        gen(n, arr, l+1, r);
        swap(arr[l], arr[i]);

    }
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++){
        arr[i] = i+1;
    }
    gen(n, arr, 0, n-1);
}