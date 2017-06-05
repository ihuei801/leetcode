class Solution {
public:
    int findMin(vector<int> &num) {

        int left = 0, right = num.size()-1;

        //notice: this is "<" instead of "<=". We compare num[left] < num[right] so left cannot be equal to right.
        while (left < right)
        {
            int mid = (left + right) >> 1;

            //left is move right sequentially. So, the first num[left] less than num[right] is the minimun one.
            if (num[left] < num[right])
                return num[left];
            if (num[mid] >= num[left])
                left = mid + 1;
            else
                right = mid;

        }
        return num[left];
    }
};