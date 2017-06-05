class Solution {
public:
    Solution(vector<int> nums) {
        init = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
       return init; 
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> re(init);
        for (int i = re.size()-1 ; i > 0; i--) {
            int randidx = rand() % (i+1);
            swap(re[i], re[randidx]);
        }
        return re;
    }
private:
    vector<int> init;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */