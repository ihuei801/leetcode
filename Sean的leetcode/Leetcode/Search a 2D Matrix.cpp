class Solution {
public:

    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int left = 0, right = matrix.size() - 1;
        int row, mid;

        if (matrix.size() == 0)
            return false;

        if (target < matrix[0][0])
            return false;

        while (left <= right)
        {
            mid = (left + right) >> 1;
            if (matrix[mid][0] == target)
                return true;
            else if (matrix[mid][0] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        row = right;
        left = 0;
        right = matrix[row].size() - 1;

        while (left <= right)
        {
            mid = (left + right) >> 1;
            if (matrix[row][mid] == target)
                return true;
            else if (matrix[row][mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return false;
    }
};