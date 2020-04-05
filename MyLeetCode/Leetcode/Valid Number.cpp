//https://leetcode.com/discuss/35947/a-clear-c-solution
class Solution {
public:
    int parse_pattern(string s, int &pos, string pattern)
    {
        if (pos < s.size() && pattern.find(s[pos]) != string::npos)
        {
            pos++;
            return 1;
        }
        else
            return 0;
    }

    void parse_space(string s, int &pos)
    {
        while(parse_pattern(s, pos, " "))
            ;
    }

    void parse_sign(string s, int &pos)
    {
        parse_pattern(s, pos, "-+");
    }

    int parse_exp(string s, int &pos)
    {
        return parse_pattern(s, pos, "eE");
    }

    int parse_dot(string s, int &pos)
    {
        return parse_pattern(s, pos, ".");
    }

    int parse_int(string s, int &pos)
    {
        if (parse_pattern(s, pos, "0123456789"))
        {
            while (parse_pattern(s, pos, "0123456789"))
                ;
            return 1;
        }
        return 0;
    }

    int parse_real(string s, int &pos)
    {
        int f1 = parse_int(s, pos);
        int f2 = parse_dot(s, pos);
        int f3 = parse_int(s, pos);

        if (f1 || (f2 && f3))
            return 1;
        return 0;
    }

    bool isNumber(string s) {
        int pos = 0;

        parse_space(s, pos);
        parse_sign(s, pos);

        if (!parse_real(s, pos))
            return false;

        if (parse_exp(s, pos))
        {
            parse_sign(s, pos);
            //if exp exists, there should be following nubmer.
            if (!parse_int(s, pos))
                return false;
        }
        parse_space(s, pos);
        return pos == s.size();
    }
};