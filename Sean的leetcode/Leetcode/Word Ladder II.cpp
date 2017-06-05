class Solution {
public:
    vector<string> genNextWords(string s, unordered_map<string, vector<string>> s_map, unordered_set<string> &wordList, unordered_set<string> &visited)
    {
        vector<string> res;
        if (s_map.count(s))
            return s_map[s];

        for (int i = 0; i < s.size(); i++)
        {
            char org_c = s[i];
            for (char c = 'a'; c <= 'z'; c++)
            {
                if (c == org_c)
                    continue;

                s[i] = c;
                if (wordList.find(s) != wordList.end())
                {
                    visited.insert(s);
                    res.push_back(s);
                }
            }
            s[i] = org_c;
        }
        return res;
    }

    vector<vector<string>> findLadders(string beginWord, string endWord, unordered_set<string> &wordList) {
        vector<vector<string> > res;
        queue<vector<string>> q;
        unordered_set<string> visited;
        unordered_map<string, vector<string>> s_map;
        vector<string> one_sol;
        int min_size = INT_MAX;
        int curr_level = 1;

        visited.insert(beginWord);
        one_sol.push_back(beginWord);
        q.push(one_sol);

        while (!q.empty())
        {
            one_sol = q.front();
            q.pop();
            string s = one_sol.back();
            vector<string> next_words;
            int size = one_sol.size();

            if (size >= min_size)
                break;
            if (curr_level == size && !visited.empty())
            {
                for (auto v : visited)
                    wordList.erase(v);
                curr_level++;
                visited.clear();
                s_map.clear();
            }

            next_words = genNextWords(s, s_map, wordList, visited);
            for (auto w : next_words)
            {
                one_sol.push_back(w);
                if (w == endWord)
                {
                    res.push_back(one_sol);
                    min_size = one_sol.size();
                    break;
                }

                q.push(one_sol);
                one_sol.pop_back();
            }
        }
        return res;
    }
};