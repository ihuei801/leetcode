class Solution {
public:
    int lengthOfLastWord(string s) {
        char last_char = ' ';
        int last_len = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != ' ')
            {
                if (last_char == ' ')
                    last_len = 1;
                else
                    last_len++;
            }
            last_char = s[i];
        }
        return last_len;
    }
};