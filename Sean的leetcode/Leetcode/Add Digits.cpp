#if 1
//Time: O(1)
//observer num from 1 to 20, and we can see the mod (%) rule.
class Solution {
public:
    int addDigits(int num) {
        return (num == 0) ? 0 : (num - 1) % 9 + 1;
    }
};
#else
class Solution {
public:
    int addDigits(int num) {
        while (num >= 10)
        {
            int sum = 0;
            for (int n = num; n; n /= 10)
                sum += n % 10;
            num = sum;
        }
        return num;
    }
};
#endif