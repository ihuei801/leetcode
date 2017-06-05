//Two max heap to keep the 2 medium numbers at each top
//add:O(logn)
//find:O(1)
//space:O(n)
class MedianFinder {
public:

    // Adds a number into the data structure.
    void addNum(int num) {
        small.push(num);
        large.push(-small.top());
        small.pop();
        if (large.size() > small.size()) {
            small.push(-large.top());
            large.pop();
        }
        
    }

    // Returns the median of current data stream
    double findMedian() {
        if (small.size() > large.size()) {
            return small.top();
        } else {
            return (small.top() - large.top()) / 2.0;
        }
    }
private:
    priority_queue<int> small;
    priority_queue<int> large;
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf;
// mf.addNum(1);
// mf.findMedian();