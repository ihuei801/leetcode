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
        if not beginWord or not endWord or not wordList:
            return 0
        if beginWord == endWord:
            return 1
        ladder = 1
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        if endWord in wordList:
            wordList.remove(endWord)
        q = collections.deque([beginWord])
        while q:
            n = len(q)
            for i in xrange(n):
                word = q.popleft()
                for i in xrange(len(word)):
                    pre = word[:i]
                    suf = word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            tmp = pre + c + suf
                            if tmp == endWord:
                                return ladder + 1
                            if tmp in wordList:
                                q.append(tmp)
                                wordList.remove(tmp)
            ladder += 1
    
        return 0