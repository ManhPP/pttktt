#include<iostream>
using namespace std;

int k;
void gen(int a[], int reqLen, int start, int currLen, bool check[], int len){
    if(currLen > reqLen)
	    return;

    else if (currLen == reqLen) 
	{
		k--;
		if (k != 0){
			return;
		}
		for (int i = 0; i < len; i++) 
		{
			if (check[i] == true) 
			{
				cout<<a[i]<<" ";
			}
		}
		return;
	}

    if (start == len) 
	{
		return;
	}

    check[start] = true;
	gen(a, reqLen, start + 1, currLen + 1, check, len);
	if (k == 0){
		return;
	}

    check[start] = false;
	gen(a, reqLen, start + 1, currLen, check, len);
	if (k == 0){
		return;
	}
}

int main(){
    int n, m;
    cin >> n;
    cin >> m;
	cin >> k;
    int arr[n];
    for (int i = 0; i < n; i++){
        arr[i] = i+1;
    }

    bool arr2[n];
    gen(arr, m, 0, 0, arr2, n);
	if (k!= 0){
		cout << -1;
	}
}