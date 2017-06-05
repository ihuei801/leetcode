// For each point i, map<distance d, count of all points at distance d from i>.
// Given that count, choose 2 (with permutation) from it, to form a boomerang with point i.
// [use long appropriately for dx, dy and key; though not required for the given test cases]

// Time Complexity: O(n^2)
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        
        int res = 0;
        int n = points.size();
        if (n <= 2) return 0;
        for (int i = 0; i < n; i++) {
            unordered_map<long, int> dis;
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                long d = distance(points[i], points[j]);
                dis[d] += 1;
            }
            for (auto p : dis) {
                res += p.second * (p.second - 1);
            }
        }
        return res;
    }
    long distance(pair<int, int>& a, pair<int, int>& b) {
        return (a.first - b.first)*(a.first - b.first) + (a.second - b.second)*(a.second - b.second);
    }
};