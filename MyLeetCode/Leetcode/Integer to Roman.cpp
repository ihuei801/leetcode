//https://leetcode.com/discuss/34945/esay-c-solution-43ms
class Solution {
public:
    string intToRoman(int num) {
        string thous[] = {"", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMMM", "MMMMMMM", "MMMMMMMM", "MMMMMMMMM"};
        string hunds[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string tens[]  = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string ones[]  = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        string res = thous[(num/1000) % 10];
        res += hunds[(num/100) % 10];
        res += tens[(num/10) % 10];
        res += ones[num%10];
        return res;
    }
};