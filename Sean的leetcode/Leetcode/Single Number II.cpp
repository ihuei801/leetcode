/*
Idea: if we look all the last bit of the numbers (assuming all are 32-bit) in the array, there must be 3k+1 or 3k '1's in total
      depending whether the single number's last bit is one or zero.
      This observation holds for all the rest 31 bits as well.
      Hence, if we sum all the numbers only at certain bit and mod by 3, we can get the corresponding bit the single number.
      Do this for all 32-bit, we can get all bits of that number.
      This generalizes the solution of LeetCode: Single Number I, where xor all the numbers is essentially trying to add all bits and then mod by 2...
*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < 32; i++)
        {
            int sum = 0;
            for (int j = 0; j < nums.size(); j++)
                sum += (nums[j] >> i) & 1;

            res |= (sum % 3) << i;
        }
        return res;
    }
};