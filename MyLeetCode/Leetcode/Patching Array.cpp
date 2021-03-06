/* Greedy
 * Let miss be the smallest sum in [0,n] that we might be missing.
 * Meaning we already know we can build all sums in [0,miss). 
 * Then if we have a number num <= miss in the given array, 
 * we can add it to those smaller sums to build all sums in [0,miss+num). 
 * If we don't, then we must add such a number to the array, 
 * and it's best to add miss itself, to maximize the reach.
 * Time Complexity: O(n)
 */
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long miss = 1;
        int cnt = 0;
        int i = 0;
        int size = nums.size();
        while (miss <= n) {
            if (i < size && nums[i] <= miss) {
                miss += nums[i++];
            }
            else {
                miss += miss;
                cnt++;
            }
        }
        return cnt;
    }
}