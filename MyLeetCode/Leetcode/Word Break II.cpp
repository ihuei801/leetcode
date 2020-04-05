s#if 1 
//DFS
//check from the end of string s
class Solution {
public:
    unordered_map<string, vector<string>> mp;

    vector<string> combine(string s, vector<string> input)
    {
        vector<string> rs;
        for (auto str: input)
            rs.push_back(s+" "+str);
        return rs;
    }

    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
        vector<string> res;
        int n = s.size();
        if (n == 0) return res;
        if (mp.count(s)) return mp[s];
        if (wordDict.count(s))
            res.push_back(s);

        for (int i = 1; i < n; i++)
        {
            string sub = s.substr(0, i);
            if (wordDict.count(sub))
            {
                vector<string> t_res = combine(sub, wordBreak(s.substr(i), wordDict));
                res.insert(res.end(), t_res.begin(), t_res.end());
            }
        }
        mp[s] = res;
        return res;
    }
};
#elif 1 //check from the end of string s
// check for the beginning of string s
//http://fisherlei.blogspot.tw/2013/11/leetcode-wordbreak-ii-solution.html
//like combination or permutation solution using recursive.
//need add short cut: possible[i]: 1: there exists solution from index i to s.size()
//                                 0: no solution from index i to s.size()
class Solution {
public:

    int genWordBreak(string s, unordered_set<string> &dict, vector<string> &res, string &one_solution, int start, vector<int> &possible)
    {
        if (start == s.size())
        {
            res.push_back(one_solution);
            return 0;
        }

        for (int i = start; i < s.size(); i++)
        {
            string str = s.substr(start, i-start+1);
            //if s[0] to s[i] is matched, then do recursive on remaining sub string.
            if (dict.find(str) != dict.end() && possible[i+1])
            {
                int pre_size = res.size();
                int pre_len = one_solution.size();

                if (one_solution.size() > 0)
                    one_solution += " ";

                one_solution += str;
                genWordBreak(s, dict, res, one_solution, i+1, possible);
                one_solution.resize(pre_len);

                //no new solution inserted
                if (pre_size == res.size())
                    possible[i+1] = 0;
            }
        }
        return 0;
    }
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        vector<vector<int> > all_idx;
        vector<int>idx;
        vector<string>res;
        string str;
        //add additional size 1 to avoid additional check,
        vector<int>possible(s.size()+1, 1);

        genWordBreak(s, dict, res, str, 0, possible);
        return res;
    }
};
#endif