//http://www.cnblogs.com/AnnieKim/archive/2013/04/25/3041982.html
//1. the definition of anagram differs from palindrome. See above link.
//2. use the sorted string as the key of hashtable.
class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {
        vector<string>res;
        map<string, int>anagram;
        
        for (int i = 0; i < strs.size(); i++)
        {
            string s = strs[i];
            sort(s.begin(), s.end());
            
            if (anagram.find(s) == anagram.end())
            {
                anagram[s] = i;
            }
            else
            {
                //if this anagram never output to res, output the first element of this anagram.
                if (anagram[s] >= 0)
                {
                    res.push_back(strs[anagram[s]]);
                    anagram[s] = -1;
                }
                res.push_back(strs[i]);
            }
        }            
        return res;
    }
};