//https://leetcode.com/discuss/43581/solutions-given-explanation-time-with-space-other-with-space
//https://leetcode.com/discuss/23835/one-pass-constant-space-java-solution
//http://fisherlei.blogspot.tw/2013/11/leetcode-candy-solution.html
//1. ascending: use pre+1 as the current candy number
//2. descending: count the total number of descending and let local mimimun with 1 candy when encountering the ascending order.
//Time: O(n), one iteration.
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        if (!n) return 0;

        int sum = 1;
        int c = 1;
        int count_down = 0;
        int pre = 1;
        //note (i == n) is to process the last count_down
        for (int i = 1; i <= n; i++)
        {
            if (i < n && ratings[i] < ratings[i-1])
                count_down++;
            else
            {
                if (count_down)
                {
                    //1+2+3...+count_down
                    sum += (count_down * (count_down+1)) >> 1;
                    //pre is the peak when descending happens.
                    if (count_down >= pre)
                        sum += count_down + 1 - pre;
                    count_down = 0;
                    pre = 1;
                }
                if (i < n)
                {
                    pre = (ratings[i] == ratings[i-1]) ? 1 : pre+1;
                    sum += pre;
                }
            }
        }
        return sum;
    }
};