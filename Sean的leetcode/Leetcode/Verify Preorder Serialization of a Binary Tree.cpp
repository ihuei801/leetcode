/*
(1)all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
(2)all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree. When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by 2, because it provides two out degrees. If a serialization is correct, diff should never be negative and diff will be zero when finished.
*/
class Solution {
public:
    bool isValidSerialization(string preorder) {
        stringstream ss(preorder);
        string str;
        int diff = 1;
        while (getline(ss, str, ',')){
            if (--diff < 0) return false;
            if (str != "#") {
                diff += 2;
            }
        }
        return diff == 0;
    }
};