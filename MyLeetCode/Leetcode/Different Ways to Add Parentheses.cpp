//https://leetcode.com/discuss/48488/c-4ms-recursive-%26-dp-solution-with-brief-explanation
//https://leetcode.com/discuss/48468/1-11-lines-python-9-lines-c
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int>left, right;
        vector<int>res;
        for (int i = 0; i < input.size(); i++)
        {
            char c = input[i];
            if (c != '+' && c != '-' && c != '*')
                continue;
            left = diffWaysToCompute(input.substr(0, i));
            right = diffWaysToCompute(input.substr(i+1));

            for (auto l : left)
                for (auto r : right)
                {
                    if (c == '+')
                        res.push_back(l+r);
                    else if (c == '-')
                        res.push_back(l-r);
                    else
                        res.push_back(l*r);
                }
        }

        if (res.size() == 0)
            res.push_back(atoi(input.c_str()));
        return res;
    }
};