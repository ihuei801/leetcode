/* Union find
 * 1D version of Number of Islands II
 */
class Solution {
public:
    int countComponents(int n, vector<pair<int, int>>& edges) {
        vector<int> root(n);
        for (int i = 0; i < n; i++) {
            root[i] = i;
        }
        for (auto e : edges) {
            int root1 = find(root, e.first);
            int root2 = find(root, e.second);
            if (root1 != root2) {
                root[root1] = root2;
                n--;
            }
        }
        return n;
    }
    int find(vector<int>& root, int idx) {
        while (root[idx] != idx) {
            root[idx] = root[root[idx]];
            idx = root[idx];
        }
        return idx;
    }
};