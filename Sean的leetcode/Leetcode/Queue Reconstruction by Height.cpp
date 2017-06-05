/*
 * Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
 * For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
 * E.g.
 * input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
 * subarray after step 1: [[7,0], [7,1]]
 * subarray after step 2: [[7,0], [6,1], [7,1]]
 */
class Solution {
public:
    static bool cmp(pair<int, int> a, pair<int, int> b) {
        if (a.first != b.first) {
            return b.first < a.first;
        }
        else {
            return b.second > a.second;
        }
    }
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        vector<pair<int, int>> res;
        int n = people.size();
        if (n <= 1) return people;
        sort(people.begin(), people.end(), cmp);
        for (auto p : people) {
            res.insert(res.begin() + p.second, p);
        }
        return res;
    }
};