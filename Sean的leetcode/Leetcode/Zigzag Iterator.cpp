class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (!v1.empty()) {
            q.push(make_pair(v1.begin(), v1.end()));
        }
        if (!v2.empty()) {
            q.push(make_pair(v2.begin(), v2.end()));
        }
    }

    int next() {
        if (hasNext()){
            vector<int>::iterator begin_it = q.front().first;
            vector<int>::iterator end_it = q.front().second;
            q.pop();
            if (begin_it + 1 != end_it) {
                q.push(make_pair(begin_it + 1, end_it));
            }
            return *begin_it;
        }
        else return -1;
    }

    bool hasNext() {
        return !q.empty();
    }
    queue<pair<vector<int>::iterator, vector<int>::iterator>> q;
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */