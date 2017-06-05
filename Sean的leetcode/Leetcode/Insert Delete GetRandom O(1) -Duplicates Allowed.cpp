//Use a hashtable with key = num, val = vector
//and a vector contains all the number
class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        bool exist = map.find(val) != map.end();
        nums.push_back(val);
        map[val].push_back(nums.size() - 1);
        return !exist;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        bool exist = map.find(val) != map.end();
        if (exist) {
            int lastnum = nums.back();
            nums.pop_back();
            int idx = map[val].back();
            map[val].pop_back();
            if (val != lastnum) {
                nums[idx] = lastnum;
                map[lastnum].back() = idx;
            }
            if (map[val].empty()) {
                map.erase(val);
            }
        }
        return exist;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
       int randidx = rand() % nums.size();
       return nums[randidx];
    }
private:
    unordered_map<int, vector<int>> map;
    vector<int> nums;
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */