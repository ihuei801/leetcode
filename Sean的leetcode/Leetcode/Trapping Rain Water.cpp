#if 1
//https://leetcode.com/discuss/16171/sharing-my-simple-c-code-o-n-time-o-1-space
//The area for each A[i]
//1. find the max height of the left of A[i], call it A_left_max[i]
//2. find the max height of the right of A[i], call it A_right_max[i]
//3. area of A[i] = (min(A_left_max[i], A_right_max[i]) - A[i])*1
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n <= 2) return 0;
        int left = 0;
        int right = height.size() - 1;
        int left_max = INT_MIN;
        int right_max = INT_MIN;
        int sum = 0;
        while (left <= right)
        {
            left_max = max(left_max, height[left]);
            right_max = max(right_max, height[right]);

            if (left_max <= right_max)
                sum += left_max - height[left++];
            else
                sum += right_max - height[right--];
        }
        return sum;
    }
};
#else
//The area for each A[i]
//1. find the max height of the left of A[i], call it A_left_max[i]
//2. find the max height of the right of A[i], call it A_right_max[i]
//3. area of A[i] = (min(A_left_max[i], A_right_max[i]) - A[i])*1
#define MIN(a, b) ((a < b) ? (a) : (b))
class Solution {
public:
    int trap(int A[], int n) {
        int total  = 0;
        int *left  = new int[n];
        int *right = new int[n];
        int max, area;

        if (n == 0) return 0;

        for (int i = 0, max = A[0]; i < n; i++)
        {
            if (max < A[i])
                max = A[i];
            left[i] = max;
        }

        for (int i = n-1, max = A[n-1]; i >= 0; i--)
        {
            if (max < A[i])
                max = A[i];
            right[i] = max;

            //Once left[i] and right[i] are all obtained, we can calculate area of A[i]
            area = MIN(left[i], right[i]) - A[i];
            if (area > 0)
                total += area;
        }

        delete left;
        delete right;
        return total;
    }
};
#endif