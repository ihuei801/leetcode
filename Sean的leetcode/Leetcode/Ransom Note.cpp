class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> appear(26);
        for (int i = 0; i < magazine.size(); i++) {
            appear[magazine[i]-'a']++;
        }
        for (int i = 0; i < ransomNote.size(); i++) {
            appear[ransomNote[i]-'a']--;
            if (appear[ransomNote[i] - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};