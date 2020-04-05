class NumArray {
public:

    vector<int> v_sum;

    NumArray(vector<int> &nums) {

        int n = nums.size();
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            v_sum.push_back(sum);
        }
    }

    int sumRange(int i, int j) {
        return i ? v_sum[j] - v_sum[i-1] : v_sum[j];
    }
};