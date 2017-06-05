// http://fisherlei.blogspot.com/2012/12/leetcode-jump-game.html
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int jump_left = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            //jump_left means the number of remaining jump when arriving at A[i].
            //So, jump_left at A[i] is the max(A[i-1], jump_left at A[i-1]) - 1
            jump_left = max(jump_left, nums[i-1]) - 1;
            if (jump_left < 0)
                return false;
        }
        return true;
    }
};