//http://www.meetqun.com/thread-8769-1-1.html
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        //to ensure n and n-1 are both >= m.
        while (n > m)
            n &= n-1;
        return n;
    }
};