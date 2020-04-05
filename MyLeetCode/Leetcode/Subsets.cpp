#if 1
//list all possible combinations
class Solution {
public:

    void do_combine(vector<int> S, vector<vector<int> >&res, vector<int> &one_comb, int start)
    {
        for (int i = start; i < S.size(); i++)
        {
            one_comb.push_back(S[i]);
            res.push_back(one_comb);
            do_combine(S, res, one_comb, i+1);
            one_comb.pop_back();
        }
    }

    vector<vector<int> > subsets(vector<int> &S)
    {

        vector<vector<int> >res;
        vector<int>one_comb;

        res.push_back(one_comb);
        sort(S.begin(), S.end());
        do_combine(S, res, one_comb, 0);
        return res;
    }
};
#elif //bit operation solution
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int> > res;
        int size = nums.size();
        int total = pow(2, size); //total combination count

        for (int i = 0; i < total; i++)
        {
            vector<int>one_sol;
            for (int j = 0; j < size; j++)
            {
                //check each bit: bit j is 1 means selecting nums[j]
                if ((1 << j) & i)
                    one_sol.push_back(nums[j]);
            }
            res.push_back(one_sol);
        }
        return res;
    }
};
#else
//use C(n, k) to solve it
class Solution {
public:

    void do_combine(vector<int> S, vector<vector<int> >&res, vector<int> &one_comb, int num, int start)
    {
        if (num == 0)
        {
            vector<int> empty;
            res.push_back(empty);
            return;
        }

        for (int i = start; i < S.size(); i++)
        {
            one_comb.push_back(S[i]);
            if (one_comb.size() == num)
            {
                res.push_back(one_comb);
                one_comb.pop_back();
                continue;
            }
            do_combine(S, res, one_comb, num, i+1);
            one_comb.pop_back();
        }
    }

    vector<vector<int> > subsets(vector<int> &S) {

        vector<vector<int> >res;
        vector<int>one_comb;

        sort(S.begin(), S.end());

        for (int i = 0; i <= S.size(); i++)
            do_combine(S, res, one_comb, i, 0);

        return res;
    }
};
#endif