class Solution {
public:
    int countPrimes(int n) {

        if (n <= 1) return 0;

        //not include n and 1
        int total = n-2;
        vector<int>num(n+1, 1);

        for (int i = 2; i < n; i++)
            for (int m = 2; i*m < n; m++)
            {
                if (num[i*m])
                {
                    total--;
                    num[i*m] = 0;
                }

            }

        return total;
    }
};
//use mod
#if 0
int countPrimes(int n) {
    map<int, int>num;

    for (int i = 2; i <= n ;i++)
        num[i] = 1;

    for (auto &itr : num)
    {
        printf("check :%d\n", itr.first);
        for (auto &itr2 : num)
        {
            if (itr2.second == 0) continue;

            if (itr2.first*itr2.first > itr.first) break;

            printf("m is :%d, %d\n", itr2.first, itr.first % itr2.first);
            if ((itr.first % itr2.first) == 0)
            {
                itr.second = 0;
                printf("m is :%d not prime\n", itr.first);
                break;
            }
        }
    }
    for (auto &m : num)
        if (m.second)
            printf("ans:%d\n", m.first);
    return 0;
}
#endif