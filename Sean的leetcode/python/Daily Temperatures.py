###
# DFS
# Time Complexity: O(n) 
# Space Complexity: O(n)
###
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st = []
        re = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                idx = st.pop()
                re[idx] = i - idx
            st.append(i)
        return re
                
                
        
        