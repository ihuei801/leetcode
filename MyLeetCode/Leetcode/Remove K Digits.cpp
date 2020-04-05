//Keep the order increasing
//pop the last element if larger
class Solution {
public:
    string removeKdigits(string num, int k) {
        string res;
        int n = num.size();
        int l = n - k;
        for (auto c : num) {
            while (k && !res.empty() && res.back() > c) {
                res.pop_back();
                k--;
            }
            res += c;
        }
        
        res.resize(l);
        int pos = res.find_first_not_of('0');
        return pos == string::npos? "0" : res.substr(pos);
    }
};