class Solution {
public:
    bool isPalindrome(int x) {
        int m = 1;
        int t = x;

        if (x < 0) return false;

        while (t / 10)
        {
            m *= 10;
            t /= 10;
        }
        while (m && (x % 10) == (x / m))
        {
            x = (x % m) / 10;
            m /= 100;
        }
        return m == 0;
    }
};