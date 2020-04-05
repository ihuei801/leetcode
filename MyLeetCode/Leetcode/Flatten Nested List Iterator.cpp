// Concept: use Stack for LIFO because we need to divide the inner list
// Iterator shouldn't copy the entire data but just iterate over the original data structure.
// keep the current progress in a stack. 
// hasNext tries to find an integer
// next returns it and moves on

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {v
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        begin.push(nestedList.begin());
        end.push(nestedList.end()); //point to the one after the last element
    }

    int next() {
        if (hasNext()){
            auto tmp = start.top();
            start.top()++;
            return tmp->getInteger();
        }
        return -1;
    }

    bool hasNext() {
        while(!begin.empty()){
            if(begin.top() == end.top()){
                begin.pop();
                end.pop();
            }
            else{
                auto x = begin.top();
                if(x->isInteger()){
                    return true;
                }
                begin.top()++;
                begin.push(x->getList().begin());
                end.push(x->getList().end());
            }
            
            
        }
        return false;
    }
private:
    stack<vector<NestedInteger>::iterator> begin, end;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */