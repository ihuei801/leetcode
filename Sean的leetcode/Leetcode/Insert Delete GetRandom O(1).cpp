/*
Use an array and an unordered_map to store the pos
*/
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (pos.count(val)) {
            return false;
        }
        nums.push_back(val);
        pos[val] = nums.size() - 1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (!pos.count(val)) {
            return false;
        }
        int p = pos[val];
        if (p != pos.size() - 1) {
            int last = nums[nums.size() - 1];
            nums[p] = last;
            pos[last] = p;
        }
        pos.erase(val);
        nums.pop_back();
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int r = rand() % nums.size();
        return nums[r];
        
    }
private:
    vector<int> nums;
    unordered_map<int, int> pos;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */