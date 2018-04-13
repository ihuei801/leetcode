###
# BFS
# Time Complexity: O(n*26L) n:number of words L:len of word
# Space Complexity: O(n)
###

###
# BFS
# Time Complexity: O(n*26L) n:number of words L:len of word
# Space Complexity: O(n)
###
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        wordList = set(wordList)
        # discard doesn't throw out error when the key doesn't exist
        wordList.discard(beginWord)
        wordList.discard(endWord)   
        ladder = 1
        q = [beginWord]
        while q:
            next_q = []
            for w in q:
                for i,e in enumerate(w):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_w = w[:i] + c + w[i+1:]
                        if new_w == endWord:
                            return ladder + 1
                        if new_w in wordList:
                            next_q.append(new_w)
                            wordList.remove(new_w)
            q = next_q
            ladder += 1
        return 0
                                        
                            
                    