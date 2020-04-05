/* Two pointers, BFS
 * start from the leave and go internal until the number of nodes <= 2
 * Time Complexity: O(n)
 */
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        vector<int> res;
        vector<unordered_set<int>> table(n);
        if (!n) return res;
        if (n == 1) return {0};
        for (auto p : edges) {
            table[p.first].insert(p.second);
            table[p.second].insert(p.first);
        }
        queue<int> q;
        for (int i = 0; i < table.size(); i++) {
            if (table[i].size() == 1) {
                q.push(i);
            }
        }
        while (n > 2) {
            int num = q.size();
            for (int i = 0; i < num; i++) {
                int tmp = q.front();
                q.pop();
                int adj = *(table[tmp].begin());
                table[adj].erase(tmp);
                if (table[adj].size() == 1) {
                    q.push(adj);
                }
            }
            n -= num;
        }
        while (!q.empty()) {
            int tmp = q.front();
            q.pop();
            res.push_back(tmp);
        }
        return res;
    }
};