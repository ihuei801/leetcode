class Solution {
public:
    int trailingZeroes(int n) {
        int count_two = 0;
        int count_five = 0;

        //remember to use long long type, otherwise int will overflow.
        for (long long i = 2; i <= n ; i *= 2)
            count_two += n/i;
        for (long long i = 5; i <= n ; i *= 5)
            count_five += n/i;

        return min(count_two, count_five);
    }
};