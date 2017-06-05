class Solution {
public:
    bool search(vector<int>& nums, int target) {

        if (nums.size() == 0)
            return false;

        int left = 0;
        int right = nums.size() - 1;

        while (left <= right)
        {
            int mid = (left + right) >> 1;

            if (nums[mid] == target || nums[left] == target || nums[right] == target)
                return true;

            //skip the duplicate number. only add this "equal condition" as compared to Search in Rotated Sorted Array
            //When nums[left] == nums[mid], we cannot decide whether nums[mid] located in the left side or right side.
            //Both sides are possible.
            if (nums[left] == nums[mid])
            {
                left++;
                continue;
            }

            //consider A[mid] in the left_region or right_region
            if (nums[mid] > nums[left])
            {
                //consider target in the ascending region or not
                if (nums[left] < target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            else
            {
                //consider target in the ascending region or not
                if (nums[mid] < target && target < nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }
        return false;
    }
};