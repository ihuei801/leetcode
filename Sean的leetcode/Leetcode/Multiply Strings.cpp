class Solution {
public:
    void addDigit(string &res, int pos, int num)
    {
        int carry = num;

        for (int i = pos; i < res.size(); i++)
        {
            int sum = carry + res[i] - '0';
            res[i] = (sum % 10) + '0';
            carry = sum / 10;
        }
        while (carry || pos == res.size())
        {
            res += (carry % 10) + '0';
            carry /= 10;
        }
    }

    string multiply(string num1, string num2) {

        if (num1 == "0" || num2 == "0") return "0";

        string res;
        int len_a = num1.size(), len_b = num2.size();
        for (int i = len_a - 1; i >= 0; i--)
            for (int j = len_b - 1; j >= 0; j--)
                addDigit(res, len_a - 1 - i + len_b - 1 - j, (num1[i]-'0')*(num2[j]-'0'));
        reverse(res.begin(), res.end());
        return res;
    }
};