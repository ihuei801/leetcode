#if 1
//https://leetcode.com/discuss/53225/c-one-pass-simple-solution
class Solution {
public:
    int nthUglyNumber(int n) {
        if (n < 0) return 0;

        vector<int> res;
        int id2, id3, id5;
        id2 = id3 = id5 = 0;

        int min_val = 1;

        while (n)
        {
            int p2, p3, p5;

            res.push_back(min_val);
            p2 = res[id2] * 2;
            p3 = res[id3] * 3;
            p5 = res[id5] * 5;
            min_val = min(p2, min(p3, p5));

            //note: we cannot use if-else here, because p2, p3, p5 may have be the same value.
            //in that case, we need to move forward those index.
            id2 += (min_val == p2);
            id3 += (min_val == p3);
            id5 += (min_val == p5);
            n--;
        }
        return res.back();
    }
};
#else
//https://leetcode.com/discuss/52809/my-solution-in-c
//https://leetcode.com/discuss/52775/my-c-solution-16-ms
class Solution {
public:
    int nthUglyNumber(int n) {
        if (n == 0) return 0;

        set<long long> n_set;
        int count = 0;

        n_set.insert(1);

        while (1)
        {
            set<long long>::iterator it = n_set.begin();
            long long t = *it;
            n_set.erase(it);

            count++;
            if (count == n)
                return t;
            n_set.insert(t * 2);
            n_set.insert(t * 3);
            n_set.insert(t * 5);
        }
    }
};
#endif