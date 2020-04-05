/* The hashtable stores the sum of all elements before index i as key, and i as value. 
 * For each i, check not only the current sum but also (currentSum - previousSum) 
 * to see if there is any that equals k, and update max length.
 */
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        int size = nums.size();
        if (size == 0) return 0;
        
        unordered_map<int, int> table;
        int maxlen = 0;
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += nums[i];
            if (sum == k) {
                maxlen = i + 1;
            }
            else if (table.count(sum - k)) {
                maxlen = max(maxlen, i - table[sum - k]);
            }
            if (table.count(sum) == 0) {
                table[sum] = i;
            }
        }
        return maxlen;
    }
};