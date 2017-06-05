d//Time complexity:O(n)
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        for (int i = n - 1; i >= 0; i--)
        {
            if (digits[i] == 9)
                digits[i] = 0;
            else
            {
                //if no carry happens, we can return the result immediately.
                digits[i]++;
                return digits;
            }
        }
        //if there's no early return, which means carry still exists.
        digits[0] = 1;
        digits.push_back(0);
        return digits;
    }
};