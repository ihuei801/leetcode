/*
 * smallidx: a prime in primes can multiply an element in ugly with the smallest index
 * Time Complexity: O(nk)
 */
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int> smallidx(primes.size(), 0);
        vector<int> ugly(n, INT_MAX);
        ugly[0] = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < primes.size(); j++) {
                ugly[i] = min(ugly[i], ugly[smallidx[j]] * primes[j]);
            }
            for (int j = 0; j < primes.size(); j++) {
                smallidx[j] += (ugly[i] == ugly[smallidx[j]] * primes[j]);
            }
        }
        return ugly[n - 1];
    }
};