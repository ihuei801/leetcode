//http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
//Time: O(n)
class Solution {
public:
    int largestRectangleArea(vector<int>& height) {
        int max_area = 0;
        stack<int> stk;
        int n = height.size();

        for (int i = 0; i < n || !stk.empty();)
        {
            if (stk.empty() || (i < n && height[stk.top()] <= height[i]))
                stk.push(i++);
            else
            {
                int x = stk.top();
                stk.pop();
                //the number of [top()+1, i-1] is (i-1) - (top() + 1) + 1 = i - 1 - top()
                int area = height[x] * (stk.empty() ? i : (i - 1 - stk.top()));
                max_area = max(max_area, area);
            }
        }
        return max_area;
    }
};