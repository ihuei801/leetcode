#if 1
//https://leetcode.com/discuss/45120/c-using-set-less-10-lines-with-simple-explanation
//We only need to care about the left-side window because the right-side window will be considered when the current
//nums[i] become a element inside the window.

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        //note: unordered_map doesn't have lower_bound() because unordered_map is not sorted.
        map<int, int>n_map;

        for (int i = 0; i < nums.size(); i++)
        {
            if (i > k)
                n_map.erase(nums[i-k-1]);

            map<int, int>::iterator it;
            it = n_map.lower_bound(nums[i]-t);
            if (it != n_map.end() && abs(it->first-nums[i]) <= t)
                return true;
            n_map[nums[i]] = i;
        }
        return false;
    }
};
#else
//https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation
//https://leetcode.com/discuss/38141/accept-c-solution
//https://leetcode.com/discuss/38195/short-c-solution

//maintain a window of size k. If the current number is nums[i], check if any number m where abs(m-nums[i]) <= t, exist in this window.
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        map<int, int>window;
        int left = 0; //record the leftmost index of in the window;

        for (int i = 0; i < nums.size(); i++)
        {
            /*if the leftmost element in window has no duplicate ones, window[nums[left]] is equal left, then we can remove it.
              otherwise, if there are duplicate nums[left] in the window, window[nums[left]] keeps the largest index one.
              We only need to care about the left-side window because the right-side window will be considered when the current
              nums[i] become a element inside the window.
            */
            if (i - left > k && window[nums[left]] == left)
            {
                window.erase(nums[left]);
                left++;
            }

            //find if any nums[i]-t to nums[i]+t exist in the window.
            //lower_bound return the first one greater or equal to nums[i]-t. so, it includes the range of nums[i]-t to nums[i]+t
            auto it = window.lower_bound(nums[i]-t);
            if (it != window.end() && abs(it->first - nums[i]) <= t)
                return true;

            window[nums[i]] = i;
        }
        return false;
    }
};
#endif