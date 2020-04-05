//https://leetcode.com/discuss/38337/my-15-line-c-code-0ms-runtime-for-test-data
#if 1
class Solution {
public:
    int rob(vector<int> &num) {
        int last1 = 0;
        int last2 = 0;
        for (int i = 0; i < num.size(); i++)
        {
            last2 = max(last1, last2 + num[i]);
            swap(last1, last2);
        }
        return max(last1, last2);
    }
};
#elif 0
//http://www.meetqun.com/thread-8777-1-1.html
class Solution {
public:
    int rob(vector<int> &num) {
        int take = 0;
        int non_take = 0;
        int max_value = 0;
        for (int i = 0; i < num.size(); i++)
        {
            take = non_take + num[i];
            non_take = max_value;
            max_value = max(take, non_take);
        }
        return max_value;
    }
};
#else

//https://leetcode.com/discuss/30079/c-1ms-o-1-space-very-simple-solution
class Solution {
public:
    int rob(vector<int> &num) {
        int max_a = 0, max_b = 0;
        for (int i = 0; i < num.size(); i++)
        {
            if ((i % 2) == 0)
            {
                max_a += num[i];
                max_a = (max_a > max_b) ? max_a: max_b;
            }
            else
            {
                max_b += num[i];
                max_b = (max_a > max_b) ? max_a: max_b;
            }
        }
        return (max_a > max_b) ? max_a: max_b;
    }
};
#endif