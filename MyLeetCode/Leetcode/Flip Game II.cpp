//https://leetcode.com/discuss/64291/share-my-java-backtracking-solution
//Time: O((n - 1) x (n - 3) x (n - 5) x ...) =  O(n!!)
class Solution {
public:
    bool canWin(string s) {
        int n = s.size();
        if (n <= 1) return false;
        for (int i = 0; i < n-1; i++) {
            if (s[i] == '+' && s[i+1] == '+') {
                string tmp = s.substr(0, i) + "--" + s.substr(i+2);
                if (!canWin(tmp)) {
                    return true;
                }
            }
        }
        return false;
    }
};


class Solution {
public:
    bool can_win(string s, unordered_map<string, bool> &mp)
    {
        if (mp.count(s)) return mp[s];

        if (s.size() < 2) return false;

        int n = s.size();
        for (int i = 0; i < n - 1; i++)
        {
            if (s[i] == '+' && s[i+1] == '+')
            {
                string t = s.substr(0, i) + "--" + s.substr(i+2);
                //if the opponent cannot win, I win.
                if (!can_win(t, mp))
                {
                    //store both t and s to speed up.
                    mp[t] = false;
                    mp[s] = true;
                    return true;
                }
            }
        }
        return false;
    }

    bool canWin(string s) {
        unordered_map<string, bool> mp;
        return can_win(s, mp);
    }
};