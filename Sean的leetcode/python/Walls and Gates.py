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
        if not rooms or not rooms[0]:
            return
        q = [(i, j) for i, row in enumerate(rooms) for j, e in enumerate(row) if e == 0]
        dis = 1
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            next_q = []
            for r, c in q:
                for dr, dc in d:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nc >= 0 and nr < len(rooms) and nc < len(rooms[0]) and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = dis
                        next_q.append((nr, nc))
            q = next_q
            dis += 1
                    
        
                            
   