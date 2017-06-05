#if 1
//KMP algorithm:  Time: O(n),  Space: O(n)
//http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
//https://leetcode.com/discuss/36807/c-8-ms-kmp-based-o-n-time-%26-o-n-memory-solution
//1. create string s+"#"+resvser_s, then calculate LPS (longest proper prefix which is also suffix)
class Solution {
public:
    string shortestPalindrome(string s) {
        string r = s;
        reverse(r.begin(), r.end());
        string str = s + "#" + r;
        //prefix[i]: store the length of longest common prefix and suffix length between [0...i].
        vector<int> prefix(str.size(), 0);

        for (int i = 1; i < str.size(); i++)
        {
            int len = prefix[i-1];
            while (len > 0 && str[i] != str[len])
                len = prefix[len-1]; //find next possible matched prefix

            if (str[i] == str[len])
                prefix[i] = len + 1;
        }
        int count = s.size() - prefix[str.size()-1];
        return r.substr(0, count) + s;
    }
};




//Sean's
class Solution {
public:
    string shortestPalindrome(string s) {
        string r = s;
        reverse(r.begin(), r.end());
        string str = s + "#" + r;
        //prefix[i]: store the length of longest common prefix and suffix length between [0...i].
        vector<int> prefix(str.size(), 0);

        for (int i = 1; i < str.size(); i++)
        {
            int len = prefix[i-1];
            while (len > 0 && str[i] != str[len])
                len = prefix[len-1]; //find next possible matched prefix

            if (str[i] == str[len])
                prefix[i] = len + 1;
        }
        int count = s.size() - prefix[str.size()-1];
        return r.substr(0, count) + s;
    }
};
#else
class Solution {
public:
    string shortestPalindrome(string s) {
        string s2=s;
        reverse(s2.begin(),s2.end());
        int n=s.size(),l;

        for (l = n; l >= 0; l--)
        {
            if(s.substr(0,l) == s2.substr(n-l))
                break;
        }
        return s2.substr(0,n-l)+s;
    }
};
#endif