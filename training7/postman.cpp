#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool sortcol( const vector<int>& v1, 
               const vector<int>& v2 ) { 
 return v1[0] > v2[0]; 
}

int main(void){
	int n, k;
    cin >> n;
	cin >> k;
	vector< vector<int> > cus1;
	vector< vector<int> > cus2;
	for(int j = 0; j < n; ++j)
	{   
        vector<int> v;
		int dis, amount;
        cin >> dis;
        cin >> amount;
        v.push_back(dis);
        v.push_back(amount);
        if (dis < 0) cus1.push_back(v);
        else cus2.push_back(v);
	}

	sort(cus1.begin(), cus1.end());
	sort(cus2.begin(), cus2.end(), sortcol);

    unsigned long long int ans = 0;
    int size1 = (int)cus1.size();
    int size2 = (int)cus2.size();

	int now = -1;
    if (!cus1.empty())
        while(now < size1 - 1){
            if (cus1[now+1][1] >= k){
                ans -= 2ll * cus1[now+1][0] * (cus1[now+1][1]/k); 
                cus1[now+1][1] %= k;
                if(!cus1[now+1][1]) now++;
            }

            if (now >= size1-1){
                break;
            }
            ans -= cus1[now+1][0] * 2ll;
            unsigned long long sum = 0;
            while (now+1 < size1 && sum + cus1[now+1][1] <= k){
                sum += cus1[++now][1];
            }
            if (now + 1 < size1){
                cus1[now+1][1] -= k-sum;
            }
        }

    now = -1;
    if (!cus2.empty())
        while(now < size2 - 1){
            if (cus2[now+1][1] >= k){
                ans += 2ll * cus2[now+1][0] * (cus2[now+1][1]/k); 
                cus2[now+1][1] %= k;
                if(!cus2[now+1][1]) now++;
            }

            if (now >= size2-1){
                break;
            }
            ans += cus2[now+1][0] * 2ll;

            unsigned long long sum = 0;
            while (now+1 < size2 && sum + cus2[now+1][1] <= k){
                sum += cus2[++now][1];
            }
            if (now+1 < size2){
                cus2[now+1][1] -= k-sum;
            }
        }

    cout<<ans;
	return 0;
}