//http://fisherlei.blogspot.tw/2013/11/leetcode-gas-station-solution.html
//http://jane4532.blogspot.tw/2013/10/gas-stationleetcode.html
// if starting from i cannot reach k, then any starting point from i+1 also cannot reach k. So, the next starting point is k+1.
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int start = 0;
        int num = gas.size();
        int curr_sum = 0;
        int total_sum = 0;

        if (!num) return -1;

        for (int i = 0; i < num; i++)
        {
            int diff = gas[i] - cost[i];
            curr_sum += diff;
            total_sum += diff;

            if (curr_sum < 0)
            {
                start = i + 1;
                curr_sum = 0;
            }
        }
        return total_sum >= 0 ? start : -1;
    }
};