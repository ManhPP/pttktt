#include <stdio.h>
#include <math.h>

const double PI = acos(-1);

int main()
{
	int n, i, f;
	double min = 0.0, max = 0.0, mid;
	double len[10001];
	int numPie, numTest;

    scanf("%d",&numTest);
    while(numTest--){
        min = 0.0;
        scanf("%d%d",&n,&f);
        f++;
        for(i = 0; i < n; i++)
        {
            scanf("%lf",&len[i]);
            len[i] *= len[i];
            max = max < len[i] ? len[i] : max; 
        }
        while(min + 1e-7< max)
        {
            mid = (max+min)/2;
            numPie = 0;
            for(i = 0; i < n; i++)
            {
                numPie += (int)floor(len[i]/mid);
            }
            if(numPie < f)
                max = mid;
            else
                min = mid;
        }
        min *= PI;
        printf("%.6lf\n",min);
    }
	return 0;
}