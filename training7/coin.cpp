#include <iostream>
using namespace std;

int deno[] = { 1, 5, 10, 50, 100, 500 };
int n = 6;

void findMin(int V)
{
	int result = 0;

	for (int i = n - 1; i >= 0; i--) {

		while (V >= deno[i]) {
			V -= deno[i];
			result++;
		}
	}

    cout << result;
}

int main()
{
	int n;
    cin >> n;
	findMin(1000 - n);
	return 0;
}
