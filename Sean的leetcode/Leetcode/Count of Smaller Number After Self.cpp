class Solution {
public:
    struct NumIndex{
        int num;
        int index;
        NumIndex(){}
        NumIndex(int n, int idx): num(n), index(idx){}
    };
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> small(n);
        vector<NumIndex> arr;
        for (int i = 0; i < n; i++) {
            arr.push_back(NumIndex(nums[i], i));
        }
        sort(arr, 0, n, small);
        return small;
    }
    void sort(vector<NumIndex>& nums, int start, int end, vector<int>& small) {
        if (end - start <= 1) return;
        int mid = start + (end - start) / 2;
        sort(nums, start, mid, small);
        sort(nums, mid, end, small);
        int len = 0;
        vector<NumIndex> cache(end - start);
        int j = mid;
        int s = 0;
        for (int i = start; i < mid; i++) {
            while (j < end && nums[j].num < nums[i].num) {
                cache[s++] = nums[j++];
            }
            cache[s++] = nums[i];
            small[nums[i].index] += j - mid;
        }
        for (int i = 0; i < s; i++) {
            nums[start + i] = cache[i];
        }
        
    }
};