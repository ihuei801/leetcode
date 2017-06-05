#if 1
//http://math.stackexchange.com/questions/425894/proof-of-closed-form-formula-to-convert-a-binary-number-to-its-gray-code
//O(1) space
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        for (int i = 0; i < (1 << n); i++)
            res.push_back(i^(i>>1));
        return res;
    }
};
#elif 1
//https://leetcode.com/discuss/30419/very-simple-c-solution-with-explanation
class Solution {
public:
    vector<int> grayCode(int n) {
        if (n == 0) return vector<int>{0};
        vector<int>res = {0, 1};

        for (int i = 2; i <= n; i++)
            for (int j = res.size()-1; j >= 0; j--)
                res.push_back(res[j] + (1 << i-1));
        return res;
    }
};
#else
//http://fisherlei.blogspot.tw/2012/12/leetcode-gray-code.html
//http://www.ugcs.caltech.edu/~wnoise/base2.html
//http://en.wikipedia.org/wiki/Gray_code
//index i, the gray code is i ^ (i >> 1)
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int>res;

        int num = 1 << n;
        res.push_back(0);
        for (int j = 1; j < num; j++)
            res.push_back(j^(j>>1));

        return res;
    }
};
#endif