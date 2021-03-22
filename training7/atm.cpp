#include <iostream>
#include <vector>
#include<math.h>
using namespace std;

void find(unsigned long long int w, int c)
{
	vector<unsigned long long int> deno;
    for (int j = 0; j <= c; j++){
        deno.push_back(1000 * pow(10, j));
        deno.push_back(2000 * pow(10, j));
        deno.push_back(3000 * pow(10, j));
        deno.push_back(5000 * pow(10, j));
    }

    int result = 0;
    int amountDeno = (int) deno.size();
	for (int i = amountDeno - 1; i >= 0; i--) {
		while (w >= deno[i]) {
			w -= deno[i];
			result++;
		}
	}

    cout << result;
    int count = 1;
    for (int i = 1; i < amountDeno; i++){

    }
}

int main()
{
	int n;
    unsigned long long int w;
    int c;

    cin >> n;
    for (int i = 0; i < n; i++){
    	cin >> w;
        cin >> c;
        find(w, c);
    }
	return 0;
}