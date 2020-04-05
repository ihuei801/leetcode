###
# Back Tracking
# Time Complexity: O(2^n) 
# Space Complexity: O(n)
###
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]
        re = []
        self.dfs(word, 0, 0, "", re)
        return re
    
    def dfs(self, word, cur, accu, one_sol, re):
        if cur == len(word):
            if accu:
                one_sol += str(accu)
            re.append(one_sol)
            return
        if accu:
            self.dfs(word, cur + 1, 0, one_sol + str(accu) + word[cur], re)
        else:
            self.dfs(word, cur + 1, 0, one_sol + word[cur], re)
        self.dfs(word, cur + 1, accu + 1, one_sol, re)
            
        
        