//https://leetcode.com/discuss/46578/java-o-n-solution-using-deque-with-explanation
//Time complexity is O(n) because each element is executed at most one time push_back() and pop_front()/pop_back(), which is O(2n) = O(n)
//Space:O(n)
//deque = double-ended queue: can insert/remove element from both sides
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int>res;
        int n = nums.size();
        if (!n || !k) return res;
        
        deque<int>window;

        for (int i = 0; i < n; i++)
        {
            if (!window.empty() && window.front() < i - k + 1)
                window.pop_front();

            while (!window.empty() && nums[window.back()] < nums[i])
                window.pop_back();

            window.push_back(i);
            if (i >= k-1)
                res.push_back(nums[window.front()]);
        }
        return res;
    }
};