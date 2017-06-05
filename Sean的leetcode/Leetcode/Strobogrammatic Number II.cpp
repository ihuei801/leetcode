//https://leetcode.com/discuss/50412/ac-clean-java-solution
class Solution {
public:
    vector<string> find(int n, int target_len)
    {
        if (n == 0) return {""};
        if (n == 1) return {"0", "1", "8"};

        vector<string> t_res = find(n-2, target_len);
        vector<string> res;

        for (auto s : t_res)
        {
            if (n != target_len)
                res.push_back("0"+s+"0");

            res.push_back("1"+s+"1");
            res.push_back("6"+s+"9");
            res.push_back("8"+s+"8");
            res.push_back("9"+s+"6");
        }
        return res;
    }

    vector<string> findStrobogrammatic(int n) {
        return find(n, n);
    }
};
