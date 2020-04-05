//http://www.cnblogs.com/jcliBlogger/p/4758761.html
//1. create the order relationship between characters.
//2. if one char whose indegree is zero, that means this char has high precedence.
//3. use BFS to implement topology sort to output char whose indegree is zero.
//https://leetcode.com/discuss/54024/straightforward-c-solution
class Solution {
public:
    string topo_sort(unordered_map<char, unordered_set<char>> &dict)
    {
        string res;
        queue<char> zero_degree;
        unordered_map<char, int> in_degree;
        for (auto m : dict)
        {
            if (!in_degree.count(m.first))
                in_degree[m.first] = 0;
            for (auto c : m.second)
                in_degree[c]++;
        }

        for (auto d : in_degree)
            if (!d.second)
                zero_degree.push(d.first);
        while (!zero_degree.empty())
        {
            char c = zero_degree.front();
            zero_degree.pop();
            res += c;
            for (auto n : dict[c])
            {
                in_degree[n]--;
                if (!in_degree[n])
                    zero_degree.push(n);
            }
        }
        return res.size() == in_degree.size() ? res : ""; //if not order found
    }

    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> dict;
        int n = words.size();

        if (!n) return "";
        if (n == 1) return words[0];

        for (int i = 1; i < n; i++)
        {
            int len1 = words[i-1].size(), len2 = words[i].size();
            int len = max(len1, len2);
            int found = 0;
            for (int j = 0;j < len; j++)
            {   //every existing char should be insert into dict
                if (j < len1 && !dict.count(words[i-1][j]))
                    dict[words[i-1][j]] = {};
                if (j < len2 && !dict.count(words[i][j]))
                    dict[words[i][j]] = {};
                // "abcf", "abdef": we can only make sure 'c' comeing before 'd'. Other char relation is unknown.
                if (j < len1 && j < len2 && words[i-1][j] != words[i][j] && !found)
                {
                    dict[words[i-1][j]].insert(words[i][j]);
                    found = 1;
                }
                if (!found && j >= len2) {
                    return "";
                }
            }
        }
        return topo_sort(dict);
    }
};