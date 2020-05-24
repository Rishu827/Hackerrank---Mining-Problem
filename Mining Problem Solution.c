#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int distance[5000];
int tons[5000];

int64_t value[5000][5000];
int64_t alpha[5000], beta[5000];

int64_t mining()
{
    int n, k, i;
    scanf("%d %d", &n, &k);
    for(i = 0; i < n; ++ i)
        scanf("%d %d", &distance[i], &tons[i]);

    for(i = 0; i < n; ++i)
    {
        int64_t lt = 0, rt = 0, md = 0;
        int s, j;

        for(j = i + 1, s = i; j < n; ++ j)
        {
            md += tons[j] * (int64_t)(distance[j] - distance[s]);
            rt += tons[j];

            while(s < j && lt + tons[s] < rt)
            {
                md += (lt + tons[s] - rt) * (int64_t)(distance[s + 1] - distance[s]);
                lt += tons[s];
                rt -= tons[s + 1];
                ++ s;
            }
            value[j][i] = md;
        }
    }

    /* memcpy(a, value[0], n * sizeof(int64_t)); */
    for(i = 0; i < n; ++ i)
        alpha[i] = value[i][0];

    if(n * (int64_t) n * (int64_t) k < 1000000000)
    {
        for(; 1 < k; --k)
            for(i = n - 1; -1 < i; --i)
            {
                int s;
                alpha[i] = value[i][0];

                for(s = 1; s < i + 1; ++ s)
                {
                    const int64_t c = alpha[s - 1] + value[i][s];
                    if(c < alpha[i]) alpha[i] = c;
                }
            }

        return alpha[n - 1];
    }

    for(; 1 < k; -- k)
    {
        int idx = 0;
        memcpy(beta, alpha, n * sizeof(int64_t));

        for(i = 0; i < n; ++ i)
        {
            alpha[i] = (idx ? beta[idx - 1] : 0) + value[i][idx];

            for(; idx < i && beta[idx] + value[i][idx + 1] < alpha[i]; ++ idx)
                alpha[i] = beta[idx] + value[i][idx + 1];

            {
                int s = i;
                for(s = i; idx < s && i < s + 50; -- s)
                {
                    const int64_t v = (s ? beta[s - 1] : 0) + value[i][s];
                    if(v < alpha[i]) alpha[i] = v;
                }

            }

        }
    }

    return alpha[n - 1];
}
int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

   

    long long result = mining();
    fprintf(fptr, "%lld\n", result);

    fclose(fptr);

    return 0;
}

