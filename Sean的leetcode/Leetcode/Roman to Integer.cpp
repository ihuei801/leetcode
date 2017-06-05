class Solution {
public:
    int symbol_to_num(char c)
    {
        switch (c)
        {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
        }
    }

    int romanToInt(string s) {
        int sum = 0;

        for (int i = 0; i < s.size(); i++)
        {
            int pre;
            int curr = symbol_to_num(s[i]);

            //for IX, we should deduct 'I' from sum.
            if (i && pre < curr)
                sum -= 2 * pre;

            sum += curr;
            pre = curr;
        }
        return sum;
    }
};