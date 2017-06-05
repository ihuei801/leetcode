class Solution {
public:
    int calculate(string s) {
        int sum = 0;
        int pre_val = 0;
        int pre_sign = 1;
        char pre_op = '+';
        int curr_val = 0;

        //last i is s.size() because we imagine to add extra '+' to the end of string to calculate the last term.
        for (int i = 0; i <= s.size(); i++)
        {
            char c;

            if (i == s.size())
                c = '+';
            else
                c = s[i];

            if (c == ' ')
                continue;

            if (isdigit(c))
                curr_val = curr_val * 10 + s[i] - '0';
            else
            {
                //check previous op
                if (pre_op == '*')
                    pre_val *= curr_val;
                else if (pre_op == '/')
                    pre_val /= curr_val;
                else
                    pre_val = curr_val;

                //if current op is '+' or '-', merge pre_val to sum.
                if (c == '+' || c =='-')
                {
                    sum += pre_sign * pre_val;
                    pre_val = 0;
                    pre_sign = c == '+' ? 1 : -1;
                }
                pre_op = c;
                curr_val = 0;
            }
        }
        return sum;
    }
};