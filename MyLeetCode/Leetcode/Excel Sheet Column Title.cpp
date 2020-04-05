#if 1 //recursive solution
class Solution {
public:
    string convertToTitle(int n) {
        return (n == 0) ? ("") : (convertToTitle((n-1) / 26) + (char)((n - 1) % 26 + 'A'));
    }
};
#else
class Solution {
public:
    string convertToTitle(int n) {
        string res;
        while (n)
        {
            res = (char)(((n-1) % 26) + 'A') + res;
            n = (n - 1) / 26;
        }
        return res;
    }
};
#endif