class Solution {
public:
    int mySqrt(int x) {
        if(x < 0) return -1;
        if(x == 0) return 0;
        long left = 1;
        long right = x;
        while(left + 1 < right){
            long mid = left + (right - left) / 2;
            if(mid * mid == x) return mid;
            else if(mid * mid < x) left = mid;
            else{
                right = mid;
            }
        }
        if(right * right <= x) return right;
        else return left;
    }
};

//Sean's
class Solution {
public:
    int mySqrt(int x) {
        long long left = 0, right = (x >> 1) + 1;

        if (x < 0) return -1;

        while (left <= right)
        {
            //use long long to prevent INT overflow.
            long long mid = (left + right) >> 1;
            long long m_square = mid * mid;

            if (x == m_square)
                return mid;
            else if (x > m_square)
                left = mid + 1;
            else
                right = mid - 1;
        }
        //break condition becomes [right, left], which means right*right < x. so, return right.
        return right;
    }
};