class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        string res;
        //use long long type to handle numerator/denominator be the value of INT_MIN.
        long long n = numerator;
        long long d = denominator;
        long long r;
        int negative = (numerator^denominator) >> 31;

        //key: the remainder (r)
        //value: the position (index) in res.
        map<long long, int>pos_table;

        if (n < 0) n = -n;
        if (d < 0) d = -d;

        //if numerator is zero, res cannot have "-".
        if (negative && n)
            res = "-";

        res += to_string(n/d);
        r = n % d;
        if (r == 0)
            return res;

        res += ".";

        while (r)
        {
            if (pos_table.count(r) > 0)
            {
                res.insert(pos_table[r], "(");
                res += ")";
                break;
            }
            pos_table[r] = res.size();
            res += to_string(10 * r / d);
            r = (10 * r) % d;
        }
        return res;
    }
};