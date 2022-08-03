from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        visited = set()
        def dfs(cnode, target, graph):
            if cnode == target:
                return True
            visited.add(cnode)
            for nnode in graph[cnode]:
                if nnode not in visited:
                    res = dfs(nnode, target,graph)
                    if res: return res
            visited.remove(cnode)
            return False
    
        
        
        for i in range(n-1, -1, -1):
            graph = {i:[]  for i in range(1, n + 1)}
            for idx, edge in enumerate(edges):
                if idx != i:
                    a, b = edge
                    graph[a].append(b)
                    graph[b].append(a)
            curedge = edges[i]
            if dfs(curedge[0], curedge[1], graph):
                return curedge
            
            
sol = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
res  = sol.findRedundantConnection(edges)
print(res)

## using union find
from typing import List


class UF:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
    
    def root(self, node):
        if self.roots[node] == node:
            return node
        else:
            return self.root(self.roots[node])
    
    def height(self, node):
        def dp(node):
            if self.roots[node] == node:
                return 1
            else:
                return 1 + dp(self.roots[node])
        return dp(node)
    
    def union(self, a, b):
        ra,  ha = self.root(a), self.height(a)
        rb, hb = self.root(b), self.height(b)
        if a < b:
            self.roots[ra] = rb
        else:
            self.roots[rb] = ra

    
    def find(self, a, b):
        if self.root(a) == self.root(b):
            return True
        return False
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n+1)
        for a, b in edges:
            if uf.find(a,b):
                return [a , b]
            else:
                uf.union(a,b)