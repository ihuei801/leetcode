//Similar to 315. Count of Smaller Numbers After Self
//Do counting when merge sort
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        if (n == 0) return 0; 
        vector<long> sums(n+1);
        for (int i = 0; i < n; i++) {
            sums[i+1] = sums[i] + nums[i];
        }
        return sort(sums, 0, n+1, lower, upper);
    }
    int sort(vector<long>& sums, int start, int end, int lower, int upper) {
        if (end - start <= 1) return 0;
        int mid = start + (end - start) / 2;
        int count = sort(sums, start, mid, lower, upper) + sort(sums, mid, end, lower, upper);
        int l = mid, r = mid, t = mid, s = 0;
        
        vector<long> cache(end - start);
        for (int i = start; i < mid; i++) {
            while (l < end && sums[l] - sums[i] < lower) l++; //l, r move from mid to end (increasing)
            while (r < end && sums[r] - sums[i] <= upper) r++;
            count += r - l;
            while (t < end && sums[t] < sums[i]) {
                cache[s++] = sums[t++]; 
            }
            cache[s++] = sums[i];
        }

        for (int i = 0; i < s; i++) {
            sums[start + i] = cache[i];
        }
        return count;
        
        
    }
};