###
# Array - Interval
# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
###
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        while i < len(A) and j < len(B):
            s = max(A[i][0], B[j][0])
            e = min(A[i][1], B[j][1])
            if s <= e:
                result.append([s, e])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return result