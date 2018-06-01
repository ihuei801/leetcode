###
# Cycle Finding
# ptn[i]: partner of label i (i can be either a seat or a person) - - ptn[i] = i + 1 if i is even; ptn[i] = i - 1 if i is odd.
# pos[i]: index of the person with label i in the row array - - row[pos[i]] == i.
# The meaning of i == ptn[pos[ptn[row[i]]]] is as follows:
# The person sitting at seat i has a label row[i], and we want to place him/her next to his/her partner.
# (1) find the label of his/her partner, which is given by ptn[row[i]].
# (2) We then find the seat of his/her partner, which is given by pos[ptn[row[i]]].
# (3) find the seat next to his/her partner's seat, which is given by ptn[pos[ptn[row[i]]]].
# Therefore, for each pivot index i, its expected index j is given by ptn[pos[ptn[row[i]]]]. 
# As long as i != j, we swap the two elements at index i and j, and continue until the placement requirement is satisfied. 
# A minor complication here is that for each swapping operation, we need to swap both the row and pos arrays.
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        if not row:
            return 0
        pos = {v: i for i, v in enumerate(row)}
        n = len(row)
        cnt = 0
        for i in xrange(0, n, 2):
            p1 = self.ptn(i)
            p2 = pos[self.ptn(row[i])] #real partner's position  
            if p1 != p2:
                cnt += 1
                pos[row[p1]], pos[row[p2]] = p2, p1
                row[p1], row[p2] = row[p2], row[p1]
        return cnt
    
    def ptn(self, i):
        return i ^ 1
        
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def ptn(i):
            return i ^ 1
        pos = [0] * len(row)
        for i, label in enumerate(row):
            pos[label] = i
        re = 0
        for i in xrange(len(row)):
            j = ptn(pos[ptn(row[i])]) 
            while j != i:
                row[i], row[j] = row[j], row[i]
                pos[row[i]], pos[row[j]] = pos[row[j]], pos[row[i]]
                re += 1
                j = ptn(pos[ptn(row[i])]) 
        return re
            
            
                                        
                            
                    