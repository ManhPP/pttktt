#include<iostream> 
using namespace std; 
	
void lis( int arr[], int n ) 
{ 
	int lis[n]; 

	lis[0] = 1; 

	for (int i = 1; i < n; i++ ) 
	{ 
		lis[i] = 1; 
		for (int j = 0; j < i; j++ ) 
			if ( arr[i] > arr[j] && lis[i] < lis[j] + 1) 
				lis[i] = lis[j] + 1; 
	} 
    int max = lis[0];
    for (int i = 0; i < n; i++){
        if (lis[i] > max){
            max = lis[i];
        }
    }

	cout << max; 
} 
	
int main() 
{ 
	int n;
    cin >> n;
    int arr[n];
    
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
	lis(arr, n);

	return 0; 
}
