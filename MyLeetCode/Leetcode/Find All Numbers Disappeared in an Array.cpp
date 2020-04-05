/*
 * The basic idea is that we iterate through the input array and mark elements as negative using nums[nums[i] -1] = -nums[nums[i]-1]. 
 * In this way all the numbers that we have seen will be marked as negative. 
 * In the second iteration, if a value is not marked as negative, it implies we have never seen that index before, so just add it to the return list.
 */
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        for (auto n : nums) {
            int v = abs(n) - 1;
            if (nums[v] > 0) {
                nums[v] = - nums[v];
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                res.push_back(i+1);
            }
        }
        return res;
    }
};