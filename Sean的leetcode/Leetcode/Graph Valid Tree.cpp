/* DFS 
 * visit: whether a node has been visited
 */
class Solution {
public:
    bool validTree(int n, vector<pair<int, int>>& edges) {
        if (n <= 1) return true;
        vector<unordered_set<int>> adj(n);
        for (auto e : edges) {
            adj[e.first].insert(e.second);
            adj[e.second].insert(e.first);
        }
        unordered_set<int> visit;
        if (hasCycle(0, -1, adj, visit)) return false;
        return visit.size() == n;
    }
    bool hasCycle(int cur, int parent, vector<unordered_set<int>>& adj, unordered_set<int>& visit) {
        if (visit.count(cur)) return true;
        visit.insert(cur);
        for (auto e: adj[cur]) {
            if (e != parent && hasCycle(e, cur, adj, visit)) return true;
        }
        return false;
    }
};
//Sean's solution
/* DFS
 * visit: check from the root whether it has loop 
 * on_path: nodes that are on the path of current dfs
 * http://www.cnblogs.com/jcliBlogger/p/4738788.html
 */
class Solution {
public:
    bool hasCycle(int idx, int parent, unordered_map<int, vector<int> > &neighbor, unordered_set<int> &visited, unordered_set<int> &on_path)
    {
        if (visited.count(idx))
            return false;

        visited.insert(idx);
        on_path.insert(idx);

        for (int i = 0; i < neighbor[idx].size(); i++)
        {
            int nb = neighbor[idx][i];
            if (nb == parent)
                continue;
            if (on_path.count(nb))
                return true;
            if (hasCycle(nb, idx, neighbor, visited, on_path))
                return true;
        }
        on_path.erase(idx);
        return false;
    }

    bool validTree(int n, vector<pair<int, int>>& edges) {
        unordered_map<int, vector<int> > neighbor;
        unordered_set<int> visited, on_path;

        for (auto p : edges)
        {
            neighbor[p.first].push_back(p.second);
            neighbor[p.second].push_back(p.first);
        }

        if (hasCycle(0, -1, neighbor, visited, on_path))
            return false;

        if (visited.size() != n)
            return false;
        return true;
    }
};
