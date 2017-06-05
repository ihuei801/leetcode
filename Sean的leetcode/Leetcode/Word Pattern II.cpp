//https://leetcode.com/discuss/63263/share-my-c-backtracking-solution
//https://leetcode.com/discuss/63252/share-my-java-backtracking-solution
//use backtracking to try all possibility in brute force way.
class Solution {
public:
    unordered_map<string, char> s_map;
    unordered_map<char, string> c_map;

    bool match(string pattern, int start_p, string str, int start_s)
    {
        int p_size = pattern.size();
        int s_size = str.size();
        if (start_p == p_size && start_s == s_size)
            return true;
        if (start_p == p_size || start_s == s_size)
            return false;
        char c = pattern[start_p];
        for (int i = start_s; i < s_size; i++)
        {
            //if s_map[w] == c && c_map[c] == w, we will not insert new entry into s_map[] or c_map[].
            int insert = 0;
            string w = str.substr(start_s, i-start_s+1);
            if (s_map.count(w))
            {
                if (s_map[w] != c)
                    continue;
            }
            else if (c_map.count(c))
            {
                if (c_map[c] != w)
                    continue;
            }
            else
            {
                insert = 1;
                s_map[w] = c;
                c_map[c] = w;
            }

            if (match(pattern, start_p+1, str, i+1))
                return true;
            if (insert)
            {
                s_map.erase(w);
                c_map.erase(c);
            }
        }
        return false;
    }

    bool wordPatternMatch(string pattern, string str) {
        return match(pattern, 0, str, 0);
    }
};