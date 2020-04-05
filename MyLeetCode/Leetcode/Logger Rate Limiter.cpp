 //Hashmap store the next timestamp we can print the word
//O(1) for the function
class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        
        if (timestamp < next[message]) {
            return false;
        }
        else{
            next[message] = timestamp + 10;
            return true;
        }
        
    }
private:
    unordered_map<string, int> next;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.shouldPrintMessage(timestamp,message);
 */