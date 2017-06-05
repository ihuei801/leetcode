class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        long long r = x;

        if (x < 0) r = -r;

        while (r)
        {
            res = res * 10 + r % 10;
            r /= 10;
        }

        if (x < 0) res = -res;

        return (res > INT_MAX || res < INT_MIN) ? 0 : res;
    }
};