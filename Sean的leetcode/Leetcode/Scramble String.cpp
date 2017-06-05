//Recursive solutions
//Time complexity:O(n^2)
//https://leetcode.com/discuss/27889/my-accepted-solution-in-6ms-little-change-in-normal-solution
//https://leetcode.com/discuss/36470/share-my-4ms-c-recursive-solution
class Solution {
public:
    bool isScramble(string s1, string s2) {
        int count[26] = {0};
        int len = s1.size();

        if (s1 == s2) return true;

        for (int i = 0; i < len; i++)
        {
            count[s1[i] - 'a']++;
            count[s2[i] - 'a']--;
        }

        //the number of each character should be the same.
        for (int i = 0; i < 26; i++)
        {
            if (count[i])
                return false;
        }

        //max i is len-1. otherwise, when s1 and s2 are not scrambled string, the program will enter infinite recursion.
        for (int i = 1; i <= len-1; i++)
        {
            //-----** and -----**
            if (isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i)))
                return true;

            //-----** and **-----
            if (isScramble(s1.substr(0, i), s2.substr(len-i)) && isScramble(s1.substr(i), s2.substr(0, len-i)))
                return true;
        }
        return false;
    }
};