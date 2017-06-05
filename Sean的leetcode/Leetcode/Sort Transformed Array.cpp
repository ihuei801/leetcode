class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        int n = nums.size();
        vector<int> re;
        if (n == 0) return re;
        re.resize(n);
        int l = 0;
        int r = n-1;
        int st = a > 0? n-1 : 0;
        while (l <= r) {
            if (a > 0) {
                if (f(nums[l], a, b, c) > f(nums[r], a, b, c)) {
                    re[st--] = f(nums[l], a, b, c);
                    l++;
                }
                else {
                    re[st--] = f(nums[r], a, b, c);
                    r--;
                }
            }
            else {
                if (f(nums[l], a, b, c) < f(nums[r], a, b, c)) {
                    re[st++] = f(nums[l], a, b, c);
                    l++;
                }
                else {
                    re[st++] = f(nums[r], a, b, c);
                    r--;
                }
            }
        }
        return re;
    }
    int f(int x, int a, int b, int c) {
        return a * x * x + b * x + c;
    }
};

/*
1.a>0, two ends in original array are bigger than center if you learned middle school math before.

2.a<0, center is bigger than two ends.

so use two pointers i, j and do a merge-sort like process. depending on sign of a, you may want to start from the beginning or end of the transformed array. For a==0 case, it does not matter what b's sign is.
The function is monotonically increasing or decreasing. you can start with either beginning or end.
*/
class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        int len = nums.size();
        vector<int> sorted(len);
        int idx = a >= 0? len - 1 : 0;
        int i = 0, j = len - 1;
        while (i <= j) {
            if (a >= 0) {
                sorted[idx--] = quad(nums[i], a, b, c) >= quad(nums[j], a, b, c)? quad(nums[i++], a, b, c) : quad(nums[j--], a, b, c);
            }
            else {
                sorted[idx++] = quad(nums[i], a, b, c) <= quad(nums[j], a, b, c)? quad(nums[i++], a, b, c) : quad(nums[j--], a, b, c);
            }
            
        }
        return sorted;
    }
    int quad(int x, int a, int b, int c) {
        return a * x * x + b * x + c;
    }
};