#if 1 //using backtracking
//https://leetcode.com/discuss/62726/c-solution-permutation-ii-with-hashmap
class Solution {
public:
    void dfs(unordered_map<char, int> &c_map, int half_size, string odd_char, string &one_sol, vector<string> &res)
    {
        if (one_sol.size() == half_size)
        {
            string rev = one_sol;
            reverse(rev.begin(), rev.end());
            res.push_back(one_sol+odd_char+rev);
            return;
        }
        for (auto &m : c_map)
        {
            if (m.second)
            {
                one_sol += m.first;
                m.second--;
                dfs(c_map, half_size, odd_char, one_sol, res);
                m.second++;
                one_sol.pop_back();
            }
        }
    }

    vector<string> generatePalindromes(string s) {
        vector<string> res;
        unordered_map<char, int> c_map;
        int odd = 0;
        string odd_char;

        for (auto c : s)
            c_map[c]++;

        int half_size = 0;
        for (auto &m : c_map)
        {
            if (m.second & 1)
            {
                odd++;
                if (odd > 1)
                    return res;
                odd_char = m.first;
            }
            m.second >>= 1;
            half_size += m.second;
        }

        string one_sol;
        dfs(c_map, half_size, odd_char, one_sol, res);
        return res;
    }
};
#elif 1 //using nextPermutation()
//http://www.cnblogs.com/jcliBlogger/p/4752065.html
//https://leetcode.com/discuss/55260/22-lines-0ms-c-easy-to-understand
class Solution {
public:
    void nextPermutation(string &str)
    {
        int n = str.size();
        int i = n - 1;
        int right = n - 1;
        for (; i > 0 && str[i-1] >= str[i]; i--)
            ;
        int left = i;
        while (left < right)
            swap(str[left++], str[right--]);

        if (i > 0)
        {
            int j = i - 1;
            while (str[i] <= str[j])
                i++;
            swap(str[i], str[j]);
        }
    }

    vector<string> generatePalindromes(string s) {
        vector<string> res;
        unordered_map<char, int> c_map;
        int odd = 0;
        string odd_char;

        for (auto c : s)
        {
            c_map[c]++;
            if (c_map[c] & 1)
                odd++;
            else
                odd--;
        }

        if (odd > 1) return res;

        string half_str;
        for (auto m : c_map)
        {
            half_str += string(m.second>>1, m.first);
            if (m.second & 1)
                odd_char = m.first;
        }
        unordered_set<string> visited;
        while (1)
        {
            if (visited.count(half_str))
                break;

            visited.insert(half_str);
            string rev = half_str;
            reverse(rev.begin(), rev.end());
            res.push_back(half_str+odd_char+rev);
            nextPermutation(half_str);
        }
        return res;
    }
};
#endif