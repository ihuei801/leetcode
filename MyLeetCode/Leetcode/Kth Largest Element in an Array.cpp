#if 1
//use partition function
//https://leetcode.com/discuss/36910/very-concise-cpp-solution-time-use-the-concept-of-quick-sort
//Time: O(N) : N + N/2 + N/4 + .... + 1 = 2N => O(N)
class Solution {
public:
    //n is the smallest n-th element
    int partition(vector<int> &nums, int left, int right, int n)
    {
        int i = left, j = right;
        int pivot = nums[left];
        while (i < j)
        {
            while (i < j && pivot <= nums[j])
                j--;
            nums[i] = nums[j];

            while (i < j && nums[i] < pivot)
                i++;
            nums[j] = nums[i];
        }

        //The 2nd while condition is "<", so the final "i" position has the "num[i] == pivot" condition.
        nums[i] = pivot;

        if (i == n-1)
            return nums[i];
        else if (i > n-1)
            return partition(nums, left, i-1, n);
        else
            return partition(nums, i+1, right, n);

    }

    int findKthLargest(vector<int>& nums, int k) {
        int size = nums.size();
        return partition(nums, 0, size-1, size-k+1);
    }
};
#elif 1 //use min_heap (priority_queue), Time: O(N*logN)
class Solution {
public:

    struct Order
    {
        bool operator() (int a, int b)
        {
            return a > b;
        }
    };

    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, Order> pq;

        for (auto n : nums)
        {
            if (pq.size() < k)
                pq.push(n);
            else if (pq.size() == k)
            {
                if (pq.top() < n)
                {
                    pq.pop();
                    pq.push(n);
                }
            }
        }
        return pq.top();
    }
};
#endif