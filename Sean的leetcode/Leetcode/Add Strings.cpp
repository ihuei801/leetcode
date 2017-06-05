class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.size() - 1;
        int j = num2.size() - 1;
        string res;
        int carry = 0;
        while (i >= 0 || j >= 0 || carry) {
            int sum = 0;
            if (i >= 0) {
                sum += num1[i] - '0';
                i--;
            }
            if (j >= 0) {
                sum += num2[j] - '0';
                j--;
            }
            sum += carry;
            carry = sum / 10;
            sum %= 10;
            res += to_string(sum);
        }
        reverse(res.begin(), res.end());
        return res;
        
    }
};