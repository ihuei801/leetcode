#if 1
//https://leetcode.com/discuss/49667/o-n-time-and-o-1-space-c-solution-with-explanation
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);

        int from_begin = 1;
        int from_end = 1;

        for (int i = 0; i < n; i++)
        {
            res[i] *= from_begin;
            from_begin *= nums[i];
            res[n-1-i] *= from_end;
            from_end *= nums[n-1-i];
        }
        return res;
    }
};
#else
//https://leetcode.com/discuss/46104/simple-java-solution-in-o-n-without-extra-space
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>res(n, 1);

        for (int i = 1; i < n; i++)
            res[i] = nums[i-1] * res[i-1];

        int right = 1;
        for (int i = n-1 ; i >= 0; i--)
        {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
};
#endif