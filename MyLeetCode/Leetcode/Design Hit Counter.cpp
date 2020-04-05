/**
hit():O(1)
getHit():O(s) s is total seconds in given time interval, in this case 300.
basic idea is using buckets. 1 bucket for every second. 
Because we only need to keep the recent hits info for 300 seconds. 
hit[] array is wrapped around by mod operation. 
Each hit bucket is associated with times[] bucket which record current time. 
If it is not current time, it means it is 300s or 600s... ago and need to reset to 1.
*/
class HitCounter {
public:
    /** Initialize your data structure here. */
    HitCounter(): hits(300), times(300) {
      
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        int idx = timestamp % 300;
        if (timestamp != times[idx]) {
            times[idx] = timestamp;
            hits[idx] = 1;
        } else {
            hits[idx]++;
        }
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        int cnt = 0;
        for (int i = 0; i < 300; i++){
            if (timestamp - times[i] < 300) {
                cnt += hits[i];
            }
        }
        return cnt;
    }
private:
    vector<int> hits;
    vector<int> times;
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
//Queue
//not good for space when multiple hits in a time
 class HitCounter {
public:
    /** Initialize your data structure here. */
    HitCounter() {
        
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */