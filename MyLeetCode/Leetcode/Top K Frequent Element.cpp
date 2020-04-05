//Time: O(n) Space: O(n)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqtable;
        for(auto e: nums){
            freqtable[e]++;
        }
        
        vector<vector<int>> bucket(nums.size() + 1);
        for(auto e: freqtable){
            bucket[e.second].push_back(e.first);
        }
        vector<int> re;
        for(int i = bucket.size()-1; i >= 0 && re.size() < k; i--){
            for(auto e : bucket[i]){
                re.push_back(e);
                if(re.size() == k){
                    break;
                }
            }
        }
        return re;
    }
};