//https://leetcode.com/discuss/26680/easy-to-understand-dp-in-java
//https://leetcode.com/discuss/29151/ac-java-solution-with-o-t-space-and-o-ts-time
class Solution {
public:
    int numDistinct(string s, string t) {
        int len_s = s.size();
        int len_t = t.size();
        int curr_count;

        if (len_s == 0) return 0;
        if (len_t == 0) return 1;

        //initialize pre_row_count vector as all 1's for the first row (i equal to 0)
        vector<int>count(len_s, 1);

        for (int i = 0; i < len_t; i++)
        {
            int pre_count = 0;
            for (int j = 0; j < len_s; j++)
            {
                if (s[j] == t[i])
                {
                    int pre_row_count;
                    if (j == 0)
                        pre_row_count = (i == 0 ? 1 : 0);
                    else
                        pre_row_count = count[j-1];
                    curr_count = pre_count + pre_row_count;
                }
                else
                    curr_count = pre_count;

                if (j > 0)
                    count[j-1] = pre_count;

                pre_count = curr_count;
            }
        }
        return curr_count;
    }
};