class Solution {
public:
    int findMin(vector<int> &num) {
        int left = 0;
        int right = num.size()-1;

        while (left < right)
        {
            int mid = (left + right) >> 1;

            if (num[left] < num[right])
                return num[left];

            if (num[mid] > num[left])
                left = mid+1;
            else if (num[mid] < num[right])
                right = mid;
            else
            {
                if (num[left] == num[mid])
                    left++;
                else if (num[right] == num[mid])
                    right--;
            }
        }
        return num[left];
    }
};