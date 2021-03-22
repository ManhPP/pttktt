#include<iostream>
using namespace std;

void gen(int a[], int reqLen, int start, int currLen, bool check[], int len){
    if(currLen > reqLen)
	    return;

    else if (currLen == reqLen) 
	{
		for (int i = 0; i < len; i++) 
		{
			if (check[i] == true) 
			{
				cout<<a[i]<<" ";
			}
		}
		cout<<"\n";
		return;
	}

    if (start == len) 
	{
		return;
	}

    check[start] = true;
	gen(a, reqLen, start + 1, currLen + 1, check, len);

    check[start] = false;
	gen(a, reqLen, start + 1, currLen, check, len);
}

int main(){
    int n, m;
    cin >> n;
    cin >> m;
    int arr[n];
    for (int i = 0; i < n; i++){
        arr[i] = i+1;
    }

    bool arr2[n];
    gen(arr, m, 0, 0, arr2, n);
}