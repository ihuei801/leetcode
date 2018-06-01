###
# Design Deque
# The taxicab distance is the number of moves required to get from point A to point B in our grid. 
# It is calculated as dist(A, B) = abs(A.x - B.x) + abs(A.y - B.y).
# Let's say we start at S, the ghost starts at G, the target is T, and the ghost catches us in the middle at X. 
# This implies dist(G, X) = dist(S, X)
# Now, if the ghost travels from G to X and then to T, it will reach T at time  dist(G, X) + dist(X, T) = dist(S, X) + dist(X, T) >= dist(G, T) 
# because of the triangle inequality that all distance metrics satisfy.
# If the ghost can intercept you in the middle, it can actually reach the target at least as early as you do. 
# So wherever the ghost starts at (and wherever the interception point is), its best chance of getting you is going directly to the target 
# and waiting there rather than intercepting you in the middle.
# Time Complexity: hasNext:  O(len of ghost)
# Space Complexity: O(1)
###
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def dis(A, B):
            return abs(A[0] - B[0]) + abs(A[1] - B[1])
        return all(dis([0, 0], target) < dis(g, target) for g in ghosts)
        
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def dis(A, B):
            return abs(A[0] - B[0]) + abs(A[1] - B[1])
        for g in ghosts:
            if dis(g, target) <= dis([0, 0], target):
                return False
        return True
                                        
                            
                    