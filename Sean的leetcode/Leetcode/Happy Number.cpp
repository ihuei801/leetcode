#if 1 //Space: O(1)
//https://leetcode.com/discuss/33055/my-solution-in-c-o-1-space-and-no-magic-math-property-involved
//https://en.wikipedia.org/wiki/Cycle_detection
class Solution {
public:
    int cal(int n)
    {
        int sum = 0;
        while (n)
        {
            int t = n % 10;
            sum += t * t;
            n /= 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        int slow = n;
        int fast = n;
        do {
            slow = cal(slow);
            fast = cal(fast);
            fast = cal(fast);
        } while (slow != fast);
        return slow == 1 ? true : false;
    }
};
#elif 1 //Space: O(n)
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> n_set;

        while (n != 1)
        {
            int sum = 0;
            while (n)
            {
                int t = n % 10;
                sum += t * t;
                n /= 10;
            }

            if (sum == 1)
                return true;
            if (n_set.count(sum))
                return false;
            n_set.insert(sum);
            n = sum;
        }
        return true;
    }
};
#endif