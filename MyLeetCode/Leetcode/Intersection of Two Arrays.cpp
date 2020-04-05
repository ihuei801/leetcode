//Use hashset 
//Time complexity: O((m+n) 
//Space complexity: O(m)
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> appear(nums1.begin(), nums1.end());
        vector<int> result;
        for(int e: nums2){
            if(appear.count(e)){
                result.push_back(e);
                appear.erase(e);
            }
        }
        return result;
    }
};