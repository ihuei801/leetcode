//update the start index by add the val and make an offset to the end+1 index 
//Time complexity:O(n+k)
class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> res(length, 0);
        for (auto e : updates) {
            int start = e[0];
            int end = e[1];
            int val = e[2];
            res[start] += val;
            if (end + 1 < length) {
                res[end + 1] -= val;
            }
        }
        
        for (int i = 1; i < length; i++) {
            res[i] += res[i-1];
        }
        return res;
    }
};