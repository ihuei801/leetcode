//keep track of the maxlen and the largest divisor's index
//Time Complexity:O(n^2)
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        vector<int> lens(n);
        vector<int> sons(n);
        sort(nums.begin(), nums.end());
        int maxlen = 0;
        int maxidx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j >= 0; j--) { //from i count down because it should count it self and let the sons not be itself
                if (nums[i] % nums[j] == 0 && lens[j] + 1 > lens[i]) {
                    lens[i] = lens[j] + 1;
                    sons[i] = j;
                }
            }
            if (lens[i] > maxlen) {
                maxlen = lens[i];
                maxidx = i;
            }
        }
        for (int i = 0; i < maxlen; i++) {
            res.push_back(nums[maxidx]);
            maxidx = sons[maxidx];
        }
        return res;
    }
};