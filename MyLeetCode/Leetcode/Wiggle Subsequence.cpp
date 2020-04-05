/*
Greedy
if the sequence is increaseing, take the first one and the last one because 
they are local min or local max
*/
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size() < 2) return nums.size();
        int maxlen = 1;
        bool increase = nums[1] > nums[0];
        for(int i = 1; i < nums.size(); i++) {
            if(increase) {
                if(nums[i] > nums[i-1]) {
                    increase = !increase;
                    maxlen++;
                }
                
            } else {
                if(nums[i] < nums[i-1]) {
                    increase = !increase;
                    maxlen++;
                }
                
            }
        }
        return maxlen;
    }
};