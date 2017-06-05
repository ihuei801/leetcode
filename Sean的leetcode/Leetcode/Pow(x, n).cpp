class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        long long pow = n;
        if (pow < 0) {
            pow = -pow;
            x = 1/x;
        }
        return (pow & 1) ? myPow(x*x, pow>>1) * x : myPow(x*x, pow>>1);
    }
};
//Sean's solution
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;

        long long exp = n;
        if (exp < 0) exp = -exp;

        double res = myPow(x, exp >> 1);
        res *= res;

        if (exp & 1)
            res *= x;

        return (n < 0) ? 1/res : res;
    }
};