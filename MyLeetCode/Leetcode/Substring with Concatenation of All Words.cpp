//https://leetcode.com/discuss/20151/an-o-n-solution-with-detailed-explanation
//Time complexity O(s.size()*words[0].size())
//1. split s into multiple segment of s.size()/words[0].size(), then each time we can move words[0].size()
//2. iterate starting position from 0 to word[0].size() - 1.
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;

        if (words.size() == 0) return res;

        int len = words[0].size();
        int num = words.size();
        int total_len = len * num;
        int j;
        unordered_map<string, int>w_map, c_map;

        for (auto w : words)
            w_map[w]++;

        for (int i = 0; i < len; i++)
        {
            int count = 0;
            int left = i;
            int right;

            c_map.clear();
            for (right = left; right < s.size() - (len - 1);)
            {
                string str = s.substr(right, len);
                if (!w_map.count(str))
                {
                    left = right = right + len;
                    c_map.clear();
                    count = 0;
                }
                else
                {
                    //each time we move len bytes
                    while (c_map[str] >= w_map[str])
                    {
                        string sub = s.substr(left, len);
                        c_map[sub]--;
                        count--;
                        left += len;
                    }
                    count++;
                    c_map[str]++;
                    right += len;
                    if (count == num)
                        res.push_back(left);
                }
            }
        }
        return res;
    }
};