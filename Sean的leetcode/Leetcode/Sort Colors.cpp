//two-pass solution: First: count number of 0's, 1's, 2's. Second: outupt each number according to their count
//one-pass solution: two pointer solution. init red_index = 0, blue_index = n-1,
//                   Once encountering red, swap it with the left_end. Once encountering blue swap it to the right_end.
//
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int pos; //the index of the "1"
        int left, right;
        pos = left = 0;
        right = nums.size() - 1;

        while (left <= right)
        {
            if (nums[left] == 2)
            {
                swap(nums[left], nums[right]);
                right--;
            }
            else if (nums[left] == 1)
                left++;
            else
            {
                if (pos != left)
                    swap(nums[pos], nums[left]);
                pos++, left++;
            }
        }
    }
};