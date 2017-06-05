//https://leetcode.com/discuss/56279/concise-standard-binary-search-solution-detailed-explanation
//Time: O(logN)
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int left = 0;
        int n = citations.size();
        int right = n - 1;

        while (left <= right)
        {
            int mid = (left + right) >> 1;

            //mid located at the right side.
            //H-index is located at the leftmost element of the right side.
            //Because if citation[i] >= n - i then the following is also true: citation[i+1] >= n - (i + 1)
            if (citations[mid] >= n - mid)
                right = mid - 1;
            //mid located at the left side.
            else
                left = mid + 1;
        }
        //finally left pointer is located at the leftmost element of the right side.
        return n - left;
    }
};