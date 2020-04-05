class Solution {
public:
    string countAndSay(int n) {
        if (n <= 1) return "1";

        string str = "1";
        string res;

        for (int i = 2; i <= n; i++)
        {
            char pre_c;
            int count = 0;
            res.clear();
            for (int j = 0; j < str.size(); j++)
            {
                if (j == 0)
                    count = 1;
                else
                {
                    if (str[j] == pre_c)
                        count++;
                    else
                    {
                        res += to_string(count) + pre_c;
                        count = 1;
                    }
                }
                pre_c = str[j];
            }
            if (count)
                res += to_string(count) + pre_c;
            str = res;
        }
        return res;
    }
};