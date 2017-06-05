
class Solution {
public:
    int findNthDigit(int n) {
        int len = 1;
        int start = 1;
        long cnt = 9;
        while (n > cnt * len) {
            n -= cnt * len;
            len++;
            start *= 10;
            cnt *= 10;
        }
        start += (n - 1) / len;
        string num = to_string(start);
        return num[(n - 1) % len] - '0';
    }
};