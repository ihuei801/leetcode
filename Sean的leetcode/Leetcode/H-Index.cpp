#if 1
// H index definition : n-i papers >= n-i citations return n - i;
// because n - i papers are located at the right side of citations[i]. Each paper's citation is >= citations[i]
// so, if citations[i] >= n - i, then n - i papers >= citations[i] >= n - i, return n-i
//Time: O(NlogN)
//Space: O(1)
//Sorted: Binary Search
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        if (n == 0) return 0;
        sort(citations.begin(), citations.end());
        int l = 0;
        int r = n-1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            int num = n - mid;
            if (citations[mid] >= num) {
                r = mid;
            }
            else {
                l = mid;
            }
        }
        if (citations[l] >= n - l) {
            return n - l;
        }
        else if (citations[r] >= n - r){
            return n - r;
        }
        return 0;
    }
};
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int n = citations.size();
        for (int i = 0; i < n; i++)
            if (citations[i] >= n - i)
                return n - i;
        return 0;
    }
};
#elif 1
//Time: O(N)
//Space: O(N)
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> cit(n+1, 0);

        for (auto c : citations)
        {
            //H-index is bounded by n because n paper >= X citations, if X > n, we still return n as H-index.
            if (c >= n)
                cit[n]++;
            else
                cit[c]++;
        }
        int sum = 0;
        for (int i = n; i >= 0; i--)
        {
            sum += cit[i];
            if (sum >= i)
                return i;
        }
        return 0;
    }
};
#endif