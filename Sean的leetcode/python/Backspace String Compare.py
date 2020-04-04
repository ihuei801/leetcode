###
# Two Pointers
# Time Complexity: O(max(S, T))
# Space Complexity: O(1)
###
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        p1, p2 = len(S) - 1, len(T) - 1
        while p1 >= 0 or p2 >= 0:
            p1 = self.find_nxt(S, p1)
            p2 = self.find_nxt(T, p2)
            if p1 < 0 and p2 < 0:
                return True
            elif p1 < 0 or p2 < 0:
                return False
            else:
                if S[p1] != T[p2]:
                    return False
            p1 -= 1
            p2 -= 1
        return p1 < 0 and p2 < 0

    def find_nxt(self, s, idx):
        skip = 0
        while idx >= 0:
            if s[idx] == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                return idx
            idx -= 1
        return idx


