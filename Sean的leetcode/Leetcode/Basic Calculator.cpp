class Solution {
public:
    int calculate(string s) {
        stack<int> sum_stk;
        stack<int> sign_stk;
        int num = 0, sum = 0;
        int sign = 1; //1: '+', -1: '-'

        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == ' ')
                continue;

            if (isdigit(s[i]))
                num = num * 10 + s[i] - '0';
            else if (s[i] == '+' || s[i] == '-')
            {
                sum += num * sign;
                num = 0;
                sign = s[i] == '+' ? 1 : -1;
            }
            else if (s[i] == '(')
            {
                sum_stk.push(sum);
                sign_stk.push(sign);
                //reset sum to 0 to calculate sum inside "()"
                sum = 0;
                num = 0;
                sign = 1;
            }
            else if (s[i] == ')')
            {
                sum += num * sign;
                int pre_sum = sum_stk.top();
                int pre_sign = sign_stk.top();
                sum_stk.pop();
                sign_stk.pop();
                pre_sum += sum * pre_sign;
                sum = pre_sum;
                //reset num to 0, ex: (1+2)+3
                num = 0;
                sign = 1;
            }
        }
        sum += num * sign;
        return sum;
    }
};