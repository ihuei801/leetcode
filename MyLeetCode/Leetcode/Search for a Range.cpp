#if 0
//recursive version
class Solution {
public:

    int search_index(int A[], int left, int right, int target)
    {
        int mid = (left + right) >> 1;

        if (left > right)
            return -1;
        if (A[mid] == target)
            return mid;
        else if (A[mid] > target)
            return search_index(A, left, mid-1, target);
        else
            return search_index(A, mid+1, right, target);
    }

    vector<int> searchRange(int A[], int n, int target) {

        int index;
        vector<int>res;
        res.clear();
        int first_idx= -1, last_idx= -1;

        index = search_index(A, 0, n-1, target);

        if (index != -1)
        {
            for (first_idx = index; first_idx >= 1 && A[first_idx-1] == target; first_idx--)
                ;

            for (last_idx = index; last_idx < n-1 && A[last_idx+1] == target; last_idx++)
                ;

        }

        res.push_back(first_idx);
        res.push_back(last_idx);
        return res;
    }

};

#else
//iterative version
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>res;
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right)
        {
            int mid = (left + right) >> 1;

            if (nums[mid] == target)
            {
                int i;
                for (i = mid; nums[i-1] == target && i-1 >= 0; i--)
                    ;
                res.push_back(i);
                for (i = mid; nums[i+1] == target && i+1 < nums.size(); i++)
                    ;
                res.push_back(i);
                return res;
            }
            else if (nums[mid] > target)
                right = mid - 1;
            else
                left = mid + 1;
        }
        res.push_back(-1);
        res.push_back(-1);
        return res;
    }
};
#endif