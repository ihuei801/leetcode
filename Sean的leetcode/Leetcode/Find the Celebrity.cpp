//https://leetcode.com/discuss/56350/straight-forward-c-solution-with-explaination
//http://www.cnblogs.com/easonliu/p/4785253.html
// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {

        if (n == 0) return -1;

        int c = 0;
        for (int i = 1; i < n; i++)
        {
            //when i is real celebrity, after c = i , c doesn't know anyone.
            if (knows(c, i))
                c = i;
        }
        for (int i = 0; i < n; i++)
        {
            if (i == c) continue;
            if (knows(c, i) || !knows(i, c))
                return -1;
        }
        return c;
    }
};