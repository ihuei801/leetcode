//https://leetcode.com/discuss/5568/does-anyone-have-better-idea-share-accepted-python-code-here
//https://leetcode.com/discuss/21027/sharing-my-straightforward-c-solution-with-explanation

// Briefly take (n,k) = (4,21) for example, in the first iteration we divide the solution set into 4 groups: "1xxx", "2xxx", "3xxx", and "4xxx", while each group has 3! = 6 members.

// From 21/6 = 3...3, we know that the 21th element is the 3rd element in the (3+1)th group. In this group, we can divide it into 3 sub-groups again: "41xx", "42xx" and "43xx", and each group has 2!=2 members.

// Then, we calculate 3/2 and get 1...1, so it's the 1st element of (1+1)nd sub-group - "421x", and now it reach the base case with only one possibility - "4213".

//The 1st number is with index 0. So, the k-th number is with index k-1.
class Solution {
public:

    string getPermutation(int n, int k) {
        string res;
        int fact[10];
        vector<char>num_set;

        fact[0] = 1;
        for (int i = 1; i < 10; i++)
        {
            fact[i] = fact[i-1] * i;
            num_set.push_back(i+'0');
        }

        while (n > 0)
        {
            int index = (k - 1) / fact[n-1];
            res += num_set[index];
            num_set.erase(num_set.begin()+index);
            k -= index * fact[n-1];
            n--;
        }
        return res;
    }
};