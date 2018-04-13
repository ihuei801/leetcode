###
# Topological sort: https://courses.csail.mit.edu/6.006/spring11/exams/notes2-2.pdf
# BFS
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
###
### Solution 1
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []
        in_degree = [0] * numCourses
        succ = collections.defaultdict(set)
        for course, pre in prerequisites:
            if course not in succ[pre]:
                succ[pre].add(course)
                in_degree[course] += 1
        re = []    
        q = [i for i, e in enumerate(in_degree) if e == 0]
        while q:
            next_q = []
            for c in q:
                re.append(c)
                for s in succ[c]:
                    in_degree[s] -= 1
                    if in_degree[s] == 0:
                        next_q.append(s)
            q = next_q
        return re if len(re) == numCourses else []

### Solution 2
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
        