class Solution {
public:
    static bool comp(int a, int b)
    {
        string ptr_a, ptr_b;
        ptr_a = to_string(a);
        ptr_b = to_string(b);

        return (ptr_a + ptr_b) > (ptr_b + ptr_a);
    }
    string largestNumber(vector<int> &num) {
        string res;
        sort(num.begin(), num.end(), comp);
        for (int i = 0; i < num.size(); i++)
        {
            if (num[0] == 0)
                return "0";
            res += to_string(num[i]);
        }
        return res;
    }
};