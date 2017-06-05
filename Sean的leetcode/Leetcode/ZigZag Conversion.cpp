//refer to http://blog.unieagle.net/2012/11/08/leetcode%E9%A2%98%E7%9B%AE%EF%BC%9Azigzag-conversion/
class Solution {
public:
    string convert(string s, int numRows) {
        string res;

        if (numRows == 0) return res;
        if (numRows == 1) return s;

        for (int i = 0; i < numRows; i++)
        {
            int k = 1;
            int j = i;
            int d = 0;
            while (1)
            {
                if (j + d < s.size())
                    res += s[j+d];
                else
                    break;

                if (i == 0 || i == numRows-1)
                    d += 2*numRows - 2;
                else
                {
                    if (k)
                        d += 2*numRows - 2 - 2*i;
                    else
                        d += 2*i;
                    k ^= 1;
                }
            }
        }
        return res;
    }
};