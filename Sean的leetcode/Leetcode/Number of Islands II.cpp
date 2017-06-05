class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
        vector<int> res;
        vector<int> roots(m * n, -1);
        vector<pair<int,int>> dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int num = 0;
        for (auto p : positions) {
            int r = p.first;
            int c = p.second;
            int idx = r * n + c;
            if (r >= 0 && r < m && c >= 0 && c < n && roots[idx] == -1){
                roots[idx] = idx;
                num++;
                for (auto d : dir) {
                    int nb_r = r + d.first;
                    int nb_c = c + d.second;
                    int nb_idx = nb_r * n + nb_c;
                    if (nb_r >= 0 && nb_r < m && nb_c >= 0 && nb_c < n && roots[nb_idx] != -1) {
                        
                        int nb_root = findRoot(roots, nb_idx), pos_root = findRoot(roots, idx);
                        if (nb_root != pos_root) {
                            roots[pos_root] = nb_root;
                            num--;
                        }
                    }
                }
            }
            res.push_back(num);
        }
        return res;
    }
    int findRoot(vector<int>& roots, int idx) {
        while (roots[idx] != idx) {
            roots[idx] = roots[roots[idx]];
            idx = roots[idx];
        }
        return idx;
    }
};