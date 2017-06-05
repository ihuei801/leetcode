/*
Binary Search
Time Complexity:O(logn)
*/
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int l = 1;
        int r = n;
        while (l + 1 < r) {
            int mid = l + (r-l) / 2;
            int res = guess(mid);
            if (res == 0) {
                return mid;
            }
            else if (res == -1) {
                r = mid;
            }
            else {
                l = mid;
            }
        }
        return guess(l) == 0? l : r; 
    }
};