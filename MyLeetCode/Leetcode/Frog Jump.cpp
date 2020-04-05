/* dfs
 * Search for the last stone in a depth-first way, prune those exceeding the [k-1,k+1] range.
 */
class Solution {
public:
    unordered_map<string, bool> table;
    bool canCross(vector<int>& stones) {
        return canCross(stones, 0, 0);
    }
    bool canCross(vector<int>& stones, int pos, int k) {
        string key = to_string(pos) + ":" + to_string(k);
        if (table.count(key)) {
            return table[key];
        }
        if (pos == stones.size() - 1) return true;
        for (int i = pos + 1; i < stones.size(); i++) {
            int gap = stones[i] - stones[pos];
            if (gap < k-1) continue;
            else if (gap > k+1) return table[key] = false;
            else if (canCross(stones, i, gap)){
                return table[key] = true;
            }
        }
        return false;
    
    }
};