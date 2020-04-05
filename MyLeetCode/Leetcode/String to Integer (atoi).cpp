class Solution {
public:
    int myAtoi(string str) {
        long long res = 0;
        int start = 0;
        int neg = 1;

        for (auto s : str)
        {
            if (!start)
            {
                if (s == ' ')
                    continue;
                else if (s == '-')
                {
                    neg = -1;
                    start = 1;
                }
                else if (s == '+')
                    start = 1;
                else if (isdigit(s))
                {
                    start = 1;
                    res = s - '0';
                }
                else
                    return 0;
            }
            else
            {
                if (isdigit(s))
                    res = res * 10 + (s - '0') * neg;
                else
                    return res;

                if (res > INT_MAX) return INT_MAX;
                if (res < INT_MIN) return INT_MIN;
            }
        }
        return res;
    }
};