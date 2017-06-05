class Solution {
public:
    int divide(int dividend, int divisor) {
        long long dend = dividend;
        long long dsor = divisor;
        long long res = 0;

        if (!dividend) return 0;

        if (dend < 0) dend = -dend;
        if (dsor < 0) dsor = -dsor;

        while (dend >= dsor)
        {
            int i = 0;
            for (long long d = dsor; dend >= d; d <<= 1)
            {
                dend -= d;
                res += 1 << i;
                i++;
            }
        }

        res = (dividend^divisor) >> 31 ? -res : res;

        if (res > INT_MAX)
            return INT_MAX;
        else if (res < INT_MIN)
            return INT_MIN;
        else
            return res;
    }
};