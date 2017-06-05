/* you should create as many trailing zeroes as you can except 3.
 */
class Solution {
public:
    int integerReplacement(int n) {
        unsigned int a = n;
        int cnt = 0;
        while (a != 1) {
            if ((a & 1) == 0) {
                a >>= 1;
            }
            else if (a == 3 || ((a >> 1) & 1) == 0) {
                a--;
            }
            else {
                a++;
            }
            cnt++;
        }
        return cnt;
    }
};