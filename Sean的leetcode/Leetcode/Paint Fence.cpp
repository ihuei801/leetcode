//https://leetcode.com/discuss/56173/o-n-time-java-solution-o-1-space
//https://leetcode.com/discuss/56173/o-n-time-java-solution-o-1-space
class Solution {
public:
    int numWays(int n, int k) {
        if (n == 0) return 0;
        if (n == 1) return k;

        int same_color = k;
        int diff_color = k * (k - 1);

        for (int i = 3; i <= n; i++)
        {
            int temp = diff_color;
            diff_color = (diff_color + same_color) * (k - 1);
            same_color = temp;
        }
        return diff_color + same_color;
    }
};