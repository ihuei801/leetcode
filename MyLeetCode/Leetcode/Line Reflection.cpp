//HashTable
class Solution {
public:
    bool isReflected(vector<pair<int, int>>& points) {
        int n = points.size();
        if (n <= 1) return true;
        unordered_map <int, set<int>> dots;
        int minv = INT_MAX;
        int maxv = INT_MIN;
        for (auto p : points) {
            minv = min(minv, p.first);
            maxv = max(maxv, p.first);
            dots[p.second].insert(p.first);
        }
        
        double line = minv + (maxv - minv) / 2.0;
        for (auto e : dots) {
            auto s = e.second;
            auto i = s.begin();
            auto j = s.end();
            j--;
            int num = s.size() / 2 + s.size() % 2;
            for (int k = 0; k < num; k++) {
                if ((*i  + *(j)) / 2.0 != line) return false;
                i++;
                j--;
            }
        }
        return true;
    }
};