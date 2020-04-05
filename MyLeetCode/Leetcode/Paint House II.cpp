//https://leetcode.com/discuss/54415/ac-java-solution-without-extra-space
//Time: O(nk), Space: O(1)
class Solution {
public:
    int minCostII(vector<vector<int> > costs) {

        int min_idx1 = -1, min_idx2 = -1;
        int n = costs.size();
        int k = costs[0].size();

        for (int i = 0; i < n; i++)
        {
            int m1 = min_idx1, m2 = min_idx2;
            min_idx1 = min_idx2 = -1;
            for (int j = 0; j < k; j++)
            {
                //if the current index is not equal to previous min cost index (i.e. different color)
                if (j != m1)
                    costs[i][j] += (m1 < 0) ? 0 : costs[i-1][m1];
                else
                    costs[i][j] += (m2 < 0) ? 0 : costs[i-1][m2];

                if (min_idx1 < 0 || costs[i][j] < costs[i][min_idx1])
                {
                    min_idx2 = min_idx1;
                    min_idx1 = j;
                }
                else if (min_idx2 < 0 || costs[i][j] < costs[i][min_idx2])
                    min_idx2 = j;
            }
        }
        return costs[n-1][min_idx1];
    }
};