//Instead of multiplying by depth, add integers multiple times 
//(by going level by level and adding the unweighted sum to the weighted sum after each level).
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int unweighted = 0, weighted = 0;
        while (!nestedList.empty()) {
            vector<NestedInteger> nextlevel;
            for (auto& e : nestedList) {
                if (e.isInteger()) {
                    unweighted += e.getInteger();
                } else {
                    vector<NestedInteger>& lst = e.getList();
                    nextlevel.insert(nextlevel.end(), lst.begin(), lst.end());
                }
            }
            weighted += unweighted;
            nestedList = nextlevel;
        }
        
        return weighted;
    }
};