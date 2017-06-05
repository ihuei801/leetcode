###
# BFS,DFS
# Time Complexit: O(n)
# Space Complexity: O(n)
###
#BFS
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        d = {node: UndirectedGraphNode(node.label)}
        q = collections.deque([node])
        while q:
            cur = q.popleft()
            for nb in cur.neighbors:
                if nb not in d:
                    d[nb] = UndirectedGraphNode(nb.label)
                    q.append(nb)
                d[cur].neighbors.append(d[nb])
        return d[node]
#DFS
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.d = {}
        return self.dfs(node)
        
    def dfs(self, node):
        if not node:
            return
        if node in self.d:
            return self.d[node]
        new_node = UndirectedGraphNode(node.label)
        self.d[node] = new_node
        for nb in node.neighbors:
            new_node.neighbors.append(self.dfs(nb))
        return new_node

