#if 1 //iterative solution
//https://leetcode.com/discuss/40508/0ms-10line-dp-c-solution-with-explain
//Time complexity:O(n^2)
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = 1;

        //i is the total node number
        for (int i = 1; i <= n; i++)
            //j is the root number
            for (int j = 1; j <= i; j++)
                //num(left_subtree)*num(right_subtree)
                dp[i] += dp[j-1]*dp[i-j];
        return dp[n];
    }
};
#else //recursive solution
class Solution {
public:
    int numTrees(int n) {

        int total = 0;

        //one combination
        if (n == 0 || n == 1)
            return 1;

        //each node can be root
        for (int i = 1; i <= n; i++)
        {
            //left subtree (1,2.. i-1), i-1 number
            int left_num = numTrees(i-1);
            //right subtree (i+1, i+2,...n), n-1 number
            int right_num = numTrees(n-i);
            total += left_num*right_num;
        }
        return total;
    }
};
