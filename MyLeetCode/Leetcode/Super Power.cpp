/*
1For example for a^5347, the above computes a^5, then a^53, then a^534, and then finally a^5347. 
And a step from one to the next can be done like a^5347 = (a^534)10 * a7.
usd a powmod function to mod 1337 before calculation
*/
class Solution {
public:
    int powmod(int a, int b){
        a %= 1337;
        int re = 1;
        for (int i = 0; i < b; i++) {
            re = (re * a) % 1337;
        }
        return re;
    }
    int superPow(int a, vector<int>& b) {
        int re = 1;
        for (int digit: b) {
            re = powmod(re, 10) * powmod(a, digit) % 1337;
        }
        return re;
    }
};