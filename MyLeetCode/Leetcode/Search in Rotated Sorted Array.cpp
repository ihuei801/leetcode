class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.empty()) return -1;
        int left = 0;
        int right = nums.size()-1;
        while(left + 1 < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target) return mid;
            else if(nums[left] < nums[mid]){
                if(target >= nums[left] && target <= nums[mid]){
                    right = mid;
                }
                else{
                    left = mid;
                }
            }
            else{
                if(target >= nums[mid] && target <= nums[right]){
                    left = mid;
                }
                else{
                    right = mid;
                }
            }
        }
        if(nums[left] == target) return left;
        if(nums[right] == target) return right;
        return -1;
    }
};

class Solution {
public:

    int search(int A[], int n, int target) {
        
        int left = 0, right = n-1;
        int mid;
        
        if (left > right)
            return -1;
            
        while (left <= right)            
        {
            mid = (left + right) >> 1;
            
            if (A[mid] == target)
                return mid;
            if (A[left] == target)
                return left;
            if (A[right] == target)
                return right;
           
            //consider A[mid] in the left_region or right_region
            if (A[mid] >= A[left])
            {
                //consider target in the ascending region or not
                if (A[left] < target && target < A[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            else
            {
                //consider target in the ascending region or not
                if (A[mid] < target && target < A[right])
                    left = mid + 1;
                else
                    right = mid - 1;                
            }
        }
        return -1;
    }   
};