</* DFS graph
 */
class Solution {
public:
    unordered_map<string, priority_queue<string, vector<string>, std::greater<string>>> edges;
    vector<string> res;
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        for (auto p : tickets) {
            edges[p.first].push(p.second);
        }
        visit("JFK");
        reverse(res.begin(), res.end());
        return res;
    }
    void visit(string dep) {
        while(!edges[dep].empty()) {
            string next = edges[dep].top();
            edges[dep].pop();
            visit(next);
        }
        res.push_back(dep);
    }
};