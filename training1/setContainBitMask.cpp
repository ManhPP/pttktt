#include<iostream>
using namespace std;

int main(){
    int n, m;
    string word;
    int i, j;
    cin >> n;
    int a[n];
    for (i = 0; i < n; i++){
        cin >> a[i];
    }

    cin >> m;
    int b[m];
    for (i = 0; i < m; i++){
        cin >> b[i];
    }

    
    for (i = 0; i < m; i++){
        for (j = 0; j< n; j++){
            if (b[i] == a[j]){
                break;
            }
        }
        if (j == n){
            cout<<0;
            return 0;
        }
    }
    cout << 1;
    return 0;
}