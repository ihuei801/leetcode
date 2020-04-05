//Time complexity:O(m+n)
//Space complexity:O(m)
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map<int, int> appear;
        vector<int> re;
        for(int e: nums1){
            if(appear.count(e)){
                appear[e]++;
            }
            else{
                appear[e] = 1;
            }
            
        }
        for(int e: nums2){
            if(appear.count(e) && appear[e] > 0){
                re.push_back(e);
                appear[e]--;
            }
        }
        return re;
    }
};