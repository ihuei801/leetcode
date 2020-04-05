//https://leetcode.com/discuss/56550/short-c-answer-and-minimize-api-calls
// Forward declaration of isBadVersion API.
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            }
            else {
                left = mid;
            }
        }
        if (isBadVersion(left)) return left;
        else return right;
    }
};

//Sean's solution
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        if (n <= 1) return n;

        while (left <= right)
        {
            int mid = left + ((right - left) >> 1);

            if (isBadVersion(mid))
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
};