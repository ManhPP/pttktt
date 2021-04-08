#include<iostream>
using namespace std;

int k;

void gen(int n, int arr[], int l, int r){
    if (l==r){
        k--;
        if ( k != 0){
            return;
        }
        for (int j=0; j < n; j++){
            cout<<arr[j]<< " ";
        }
        return;
    }

    for (int i = l; i <= r; i++){
        swap(arr[l], arr[i]);
        gen(n, arr, l+1, r);
        if (k==0){
            return;
        }
        swap(arr[l], arr[i]);

    }
}

int main(){
    int n;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++){
        arr[i] = i+1;
    }
    gen(n, arr, 0, n-1);
    if (k!=0){
        cout << -1;
    }
}