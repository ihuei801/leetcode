###
# BFS,DFS
# Time Complexit: O(n)
# Space Complexity: O(n)
###
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
        if not node:
            return None
        return self.dfs(node, dict())
    def dfs(self, node, d):
        d[node] = UndirectedGraphNode(node.label)
        for nb in node.neighbors:
            if nb not in d:
                nbclone = self.dfs(nb, d)
            else:
                nbclone = d[nb]
            d[node].neighbors.append(nbclone)
        return d[node]
        
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
        return self.dfs(node, dict())

    def dfs(self, node, d):
        if node in d:
            return d[node]
        d[node] = UndirectedGraphNode(node.label)
        for nb in node.neighbors:
            d[node].neighbors.append(self.dfs(nb, d))
        return d[node]
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
        q = [node]
        d = {node:UndirectedGraphNode(node.label)}
        while q:
            next_q = []
            for e in q:
                for nb in e.neighbors:
                    if nb not in d:
                        d[nb] = UndirectedGraphNode(nb.label)
                        next_q.append(nb)
                    d[e].neighbors.append(d[nb])
            q = next_q
        return d[node]

