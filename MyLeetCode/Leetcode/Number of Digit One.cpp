//https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-python
class Solution {
public:
    int countDigitOne(int n) {
        int count = 0;
        for (long long m = 1; m <= n; m *= 10)
        {
            /*case1: n = 3141520, m = 100, a = 31415, b = 20
                     count = (3141+1)*100
              case2: n = 3141120, m = 100, a = 31411, b = 20
                     count = 3141*100 + (20 + 1)
              case3: n = 3141020, m = 100, a = 31410, b = 20
                     count = 3141*100
            */
            int a = n/m, b = n%m;
            // (a+8) => make 3141 to be 3142
            // ((a%10) == 1) * (b+1) => if last digit of a is 1, we need to add partial 1.
            count += (a + 8) / 10 * m + ((a%10) == 1) * (b+1);
        }
        return count;
    }
};