###
# BFS
# Time Complexity: O(VE)
# Space Complexity: O(VE)
###
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        succ = collections.defaultdict(set)
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            if course not in succ[pre]:
                succ[pre].add(course)
                in_degree[course] += 1
        q = collections.deque([ i for i,e in enumerate(in_degree) if e == 0])
        re = []
        while q:
            c = q.popleft()
            re.append(c)
            for nb in succ[c]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                   q.append(nb)
        return re if len(re) == numCourses else []
        