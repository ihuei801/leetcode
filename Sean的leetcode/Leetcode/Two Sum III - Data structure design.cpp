class TwoSum {
public:
    unordered_map<int, int> n_map;
    // Add the number to an internal data structure.
    void add(int number) {
        n_map[number]++;
    }

    // Find if there exists any pair of numbers which sum is equal to the value.
    bool find(int value) {
        for (auto n : n_map)
        {
            int diff = value - n.first;
            if ((diff != n.first && n_map.count(diff))
                || (diff == n.first && n_map[diff] >= 2))
                return true;
        }
        return false;
    }
};


// Your TwoSum object will be instantiated and called as such:
// TwoSum twoSum;
// twoSum.add(number);
// twoSum.find(value);