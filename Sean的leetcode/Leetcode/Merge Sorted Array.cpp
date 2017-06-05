class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m+n-1;
        while (i >= 0 && j >= 0)
        {
            if (nums1[i] > nums2[j])
                nums1[k--] = nums1[i--];
            else
                nums1[k--] = nums2[j--];
        }
        //if i >= 0, nums1[0] to nums1[i] are already at nums1[]. So no need to move them.
        while(j >= 0)
            nums1[k--] = nums2[j--];
    }
};