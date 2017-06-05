#if 1
//https://leetcode.com/discuss/65510/simple-java-code-without-sorting
//Time: O(mn) without sorting
class Solution {
public:
    int findMinDist(vector<vector<int>>& grid, int dir)
    {
        int max_row = grid.size();
        int max_col = grid[0].size();
        vector<int> nums;

        if (!dir)
        {
            //ensure row index is ascending order in nums
            for (int i = 0; i < max_row; i++)
                for (int j = 0; j < max_col; j++)
                {
                    if (grid[i][j])
                        nums.push_back(i);
                }
        }
        else
        {
            //ensure col index is ascending order in nums
            for (int j = 0; j < max_col; j++)
                for (int i = 0; i < max_row; i++)
                {
                    if (grid[i][j])
                        nums.push_back(j);
                }
        }

        int sum = 0;
        int left = 0, right = nums.size() - 1;
        while (left < right)
            sum += nums[right--] - nums[left++];
        return sum;
    }

    int minTotalDistance(vector<vector<int>>& grid) {
        return findMinDist(grid, 0) + findMinDist(grid, 1);
    }
};
#elif 1
//https://leetcode.com/discuss/65336/14ms-java-solution
//Time: O(mn + mlogm + m + nlogn + n)
class Solution {
public:
    int findMinDist(vector<int> & nums)
    {
        sort(nums.begin(), nums.end());
        int left = 0;
        int right = nums.size() - 1;
        int sum = 0;
        while (left < right)
            sum += nums[right--] - nums[left++];
        return sum;
    }

    int minTotalDistance(vector<vector<int>>& grid) {
        int sum = 0;
        vector<int> row, col;
        int max_row = grid.size();

        if (!max_row) return -1;

        int max_col = grid[0].size();
        for (int i = 0; i < max_row; i++)
            for (int j = 0; j < max_col; j++)
            {
                if (grid[i][j])
                {
                    row.push_back(i);
                    col.push_back(j);
                }
            }
        return findMinDist(row) + findMinDist(col);
    }
};
#endif