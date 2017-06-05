//Use queue for FIFO 
class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size):size(size),sum(0) {
        
    }
    
    double next(int val) {
        if (q.size() == maxsize) {
            sum -= q.front();
            q.pop();
        }
        q.push(val);
        sum += val;
        return sum / nums.size();
    }
private:
    double sum;
    int size;
    queue<int> nums;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */