//https://leetcode.com/discuss/30647/single-loop-simple-java-solution
class Solution {
public:
    int jump(vector<int>& nums) {
        int reachable = 1;
        int left = 0;
        int next_pos = 0; //next reachable position
        int max_pos = 0;  //max reachable position before encountering the next_pos
        int step = 0;

        //this is jump game 1 to decide whether it is reachable or not.
        //note: index starts from 1.
        for (int i = 1; i < nums.size(); i++)
        {
            left = max(left, nums[i-1]) - 1;
            if (left < 0)
            {
                reachable = 0;
                break;
            }
        }

        if (!reachable) return 0;

        //note: end condition is size() - 1 because we don't want to do step++ on nums[nums.size()-1].
        for (int i = 0; i < nums.size() - 1; i++)
        {
            max_pos = max(max_pos, i + nums[i]);
            if (i == next_pos)
            {
                step++;
                next_pos = max_pos;
            }
        }
        return step;
    }
};