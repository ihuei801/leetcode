//use bit-representation to represent substring to speed up.
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        map<int, int>num_table;
        map<char, int>char_to_num;
        vector<string>res;
        int num = 0;

        char_to_num['A'] = 0; //00
        char_to_num['C'] = 1; //01
        char_to_num['G'] = 2; //10
        char_to_num['T'] = 3; //11

        for (int i = 0; i < s.size(); i++)
        {
            //each character is represented in 2-bits. (mask the highest 12-bits and lowest 2-bits)
            num = ((num << 2) & 0xffffc) | char_to_num[s[i]];

            //not reach 10-character.
            if (i < 9)
                continue;

            if (num_table.count(num) > 0)
            {
                if (num_table[num] == 1)
                {
                    res.push_back(s.substr(i-9, 10));
                    num_table[num] = 2;
                }
            }
            else
                num_table[num] = 1;
        }
        return res;
    }
};