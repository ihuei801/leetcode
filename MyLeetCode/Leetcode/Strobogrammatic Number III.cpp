//https://leetcode.com/discuss/50624/clean-and-easy-understanding-java-solution
//http://likemyblogger.blogspot.com/2015/08/leetcode-248-strobogrammatic-number-iii.html
//C++: 104 ms
class Solution {
public:
    unordered_map<char, char> mp;

    int mycmp(string &a, string &b)
    {
        if (a.size() > b.size())
            return 1;
        else if (a.size() < b.size())
            return -1;
        else
            return a.compare(b);
    }

    void dfs(string str, string low, string high, int left, int right, int &count)
    {
        if (left > right)
        {
            if ((str[0] != '0' || str.size() == 1) && mycmp(low, str) <= 0 && mycmp(str, high) <= 0)
                count++;
            return;
        }

        for (auto m : mp)
        {
            str[left] = m.first;
            str[right] = m.second;
            if (left < right || (left == right && m.first == m.second))
                dfs(str, low, high, left+1, right-1, count);
        }
    }

    int strobogrammaticInRange(string low, string high) {
        mp['0'] = '0';
        mp['1'] = '1';
        mp['8'] = '8';
        mp['6'] = '9';
        mp['9'] = '6';
        int low_len = low.size();
        int high_len = high.size();
        int count = 0;
        for (int i = low_len; i <= high_len; i++)
        {
            string str(i, ' ');
            dfs(str, low, high, 0, i-1, count);
        }
        return count;
    }
};