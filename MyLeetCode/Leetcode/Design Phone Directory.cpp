class PhoneDirectory {
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) {
        max_num = maxNumbers;
        for (int i = 0; i < maxNumbers; i++) {
            available.push(i);
        }
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() {
        if (available.empty()) {
            return -1;
        }
        int num = available.front();
        available.pop();
        used.insert(num);
        return num;
    }
    
    /** Check if a number is available or not. */
    bool check(int number) {
        if (number >= max_num || number < 0) return false;
        return !used.count(number);
    }
    
    /** Recycle or release a number. */
    void release(int number) {
        if (used.count(number)){
            used.erase(number);
            available.push(number);
        }
    }
private:
    unordered_set<int> used;
    queue<int> available;
    int max_num;
     
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * bool param_2 = obj.check(number);
 * obj.release(number);
 */