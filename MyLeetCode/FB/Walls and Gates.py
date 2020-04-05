###
# BFS
# Time Complexity: O(mn)
# Space Complexity: O(mn)
###
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        #time O(m*n)
        #Space O(m*n)
        if not rooms or not rooms[0]:
            return
        q = []
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        dis = 1
        while q:
            next_q = []
            for (r,c) in q:
                for (nb_r, nb_c) in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0 <= nb_r < len(rooms) and 0 <= nb_c < len(rooms[0]) and rooms[nb_r][nb_c] == 2147483647:
                        rooms[nb_r][nb_c] = dis
                        next_q.append((nb_r, nb_c))
            dis += 1
            q = next_q
            
                        
                
   