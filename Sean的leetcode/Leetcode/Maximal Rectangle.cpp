//https://leetcode.com/discuss/17993/sharing-straightforward-solution-with-time-with-explanation
//use the concept of "Largest Rectangle in Histogram"
class Solution {
public:

    int getMaxArea(vector<int> &heights)
    {
        int max_area = 0;
        stack<int>stk;
        int h, area;
        int i;
        for (i = 0; i < heights.size();)
        {
            if (stk.empty() || heights[stk.top()] <= heights[i])
            {
                stk.push(i);
                i++;
            }
            else
            {
                h = stk.top();
                stk.pop();
                area = heights[h] * (stk.empty() ? i : i - 1 - stk.top());
                max_area = max(max_area, area);
            }
        }

        while (!stk.empty())
        {
            h = stk.top();
            stk.pop();
            area = heights[h] * (stk.empty() ? i : i - 1 - stk.top());
            max_area = max(max_area, area);
        }
        return max_area;
    }

    int maximalRectangle(vector<vector<char>>& matrix) {

        int row = matrix.size();

        if (!row)
            return 0;

        int col = matrix[0].size();
        vector<int> heights(matrix[0].size(), 0);
        int max_area = 0;

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (matrix[i][j] == '0')
                    heights[j] = 0;
                else
                    heights[j]++;
            }
            max_area = max(max_area, getMaxArea(heights));
        }
        return max_area;
    }
};