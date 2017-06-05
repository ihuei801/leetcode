 /*dfs*/
 class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> res;
        string one_sol;
        if (num.empty()) return res;
        dfs(num, 0, target, one_sol, 0, 0, res);
        return res;
    }
    void dfs(string num, int cur, int target, string one_sol, int sum, int multed, vector<string>&res) {
        if (cur == num.size()) {
            if (sum == target) {
                res.push_back(one_sol);
            }
            return;
        }
        
        for (int i = cur; i < num.size(); i++) {
            if (i != cur && num[cur] == '0') {
                break;
            }
            string tmp = num.substr(cur, i - cur + 1);
            long long val = stoll(tmp, 0, 10);
            if (val > INT_MAX || to_string(val) != tmp)
                break;
            if (cur == 0) {
                dfs(num, i + 1, target, one_sol + tmp, sum + val, val, res);
            }
            else {
                dfs(num, i + 1, target, one_sol + "+" + tmp, sum + val, val, res);
                dfs(num, i + 1, target, one_sol + "-" + tmp, sum - val, -val, res);
                dfs(num, i + 1, target, one_sol + "*" + tmp, sum - multed + multed * val, multed * val, res);
            }
        }
    }
};
//Sean's solution
//https://leetcode.com/discuss/58535/17-lines-solution-dfs-c
class Solution {
public:

    void dfs(string num, int start, int target, string one_sol, vector<string> &res, int sum, int pre_val, char pre_op)
    {
        if (start == num.size())
        {
            if (sum == target)
                res.push_back(one_sol);
            return;
        }

        for (int i = start; i < num.size(); i++)
        {
            string sub_str = num.substr(start, i-start+1);
            long long curr_v = stoll(sub_str, 0, 10);

            if (curr_v > INT_MAX || to_string(curr_v) != sub_str)
                break;

            dfs(num, i+1, target, one_sol+"+"+sub_str, res, sum+curr_v, curr_v, '+');
            dfs(num, i+1, target, one_sol+"-"+sub_str, res, sum-curr_v, curr_v, '-');

            if (pre_op == '+')
                dfs(num, i+1, target, one_sol+"*"+sub_str, res, sum-pre_val+pre_val*curr_v, pre_val*curr_v, '+');
            else if (pre_op == '-')
                dfs(num, i+1, target, one_sol+"*"+sub_str, res, sum+pre_val-pre_val*curr_v, pre_val*curr_v, '-');
        }
    }

    vector<string> addOperators(string num, int target) {
        string one_sol;
        vector<string> res;

        for (int i = 0; i < num.size(); i++)
        {
            one_sol = num.substr(0, i+1);
            long long curr_v = stoll(one_sol, 0, 10);
            if (curr_v > INT_MAX || to_string(curr_v) != one_sol)
                break;
            dfs(num, i+1, target, one_sol, res, curr_v, curr_v, '+');

            //it should consider the test case of ("2147483648", -2147483648) but leetcode doesn't check it.
            //dfs(num, i+1, target, "-"+one_sol, res, -curr_v, curr_v, '-');
        }
        return res;
    }
};