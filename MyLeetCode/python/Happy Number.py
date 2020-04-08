"""
Fast & Slow pointer
Time Complexity: O(n)
Space Complexity:O(2)
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        s = f = n
        while True:
            f = self.get_next_num(self.get_next_num(f))
            s = self.get_next_num(s)
            if f == s:
                break
        return s == 1

    def get_next_num(self, n):
        nxt = 0
        while n > 0:
            d = n % 10
            nxt += d * d
            n //= 10  # //: floor division
        return nxt

                            
                    