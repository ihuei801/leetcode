class Solution {
public:
    string addBinary(string a, string b) {
        string s;
        int i = a.size() - 1, j = b.size() - 1;
        int c = 0;
        while (i >= 0 || j >= 0 || c) {
            c += i >= 0? a[i--] - '0' : 0;
            c += j >= 0? b[j--] - '0' : 0;
            s = char(c % 2 + '0') + s;
            c /= 2;
        }
        return s;
    }
};

class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int len_a = a.size();
        int len_b = b.size();
        int c = 0;
        for (int i = len_a-1, j = len_b-1; i >= 0 || j >= 0 || c;)
        {
            int num_a = i >= 0 ? a[i] - '0' : 0;
            int num_b = j >= 0 ? b[j] - '0' : 0;
            res = to_string(num_a^num_b^c) + res;
            c = (num_a && num_b) || (num_a && c) || (num_b && c);
            i = i >= 0 ? i - 1 : -1;
            j = j >= 0 ? j - 1 : -1;
        }
        return res;
    }
};