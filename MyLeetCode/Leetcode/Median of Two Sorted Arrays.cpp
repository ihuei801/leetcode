//https://leetcode.com/discuss/30807/o-lg-m-n-c-solution-using-kth-smallest-number
//Time: O(log(m+n))
class Solution {
public:
    //The first element is 1th. K is not index number.
    int getKth(vector<int>::iterator it1, int size1, vector<int>::iterator it2, int size2, int k)
    {
        //because we use size1 to decide the smallest i-th number (i), so we have to ensure size2 is larger than size1.
        //otherwise, j may be larger than maximun number in it2 (size2) which is invalid.
        if (size1 > size2) return getKth(it2, size2, it1, size1, k);

        if (size1 == 0) return *(it2+k-1);
        if (k == 1) return min(*it1, *it2);

        int i = min(size1, k >> 1);
        int j = k - i;

        //remove the smaller i elements
        if (*(it1 + i - 1) < *(it2 + j - 1))
            return getKth(it1+i, size1-i, it2, size2, k-i);
        else
            return getKth(it1, size1, it2+j, size2-j, k-j);
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        int mid = (n + m) >> 1;

        if ((m + n) & 1)
            return getKth(nums1.begin(), n, nums2.begin(), m, mid+1);
        else
            return ((double)getKth(nums1.begin(), n, nums2.begin(), m, mid)
                   + (double)getKth(nums1.begin(), n, nums2.begin(), m, mid+1)) / 2;
    }
};