// For org to be uniquely reconstructible from seqs we need to satisfy 2 conditions:

// Every sequence in seqs should be a subsequence in org. This part is obvious.
// Every 2 consecutive elements in org should be consecutive elements in some sequence from seqs. Why is that? Well, suppose condition 1 is satisfied. Then for 2 any consecutive elements x and y in org we have 2 options.
// We have both xand y in some sequence from seqs. Then (as condition 1 is satisfied) they must be consequtive elements in this sequence.
// There is no sequence in seqs that contains both x and y. In this case we cannot uniquely reconstruct org from seqs as sequence with x and y switched would also be a valid original sequence for seqs.
// So this are 2 necessary criterions. It is pretty easy to see that this are also sufficient criterions for org to be uniquely reconstructible (there is only 1 way to reconstruct sequence when we know that condition 2 is satisfied).

// To implement this idea I have idxs hash that maps item to its index in org sequence to check condition 1. And I have pairs set that holds all consequitive element pairs for sequences from seqs to check condition 2 (I also consider first elements to be paired with previous undefined elements, it is necessary to check this).
class Solution {
public:
    bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {
        unordered_map<int, int> idx;
        unordered_set<string> pairs;
        for (int i = 0; i < org.size(); i++) {
            idx[org[i]] = i;
        }
        for (auto seq : seqs) {
            for (int i = 0; i < seq.size(); i++) {
                if (!idx.count(seq[i])) return false;
                if (i > 0 && idx[seq[i]] <= idx[seq[i-1]]) return false;
                if (i > 0)
                    pairs.insert(to_string(seq[i-1]) + "," + to_string(seq[i]));
                else
                    pairs.insert(to_string(seq[i]));
            }
        }
        for (int i = 0; i < org.size(); i++) {
            if (i > 0) {
                if (!pairs.count(to_string(org[i-1]) + "," + to_string(org[i]) )) return false;
            }
            else {
                if (!pairs.count(to_string(org[i]))) return false;
            }
        }
        return true;
    }
};