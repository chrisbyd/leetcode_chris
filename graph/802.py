from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        tnodes = set()
        n = len(graph)
        for i in range(n):
            if not graph[i]:
                tnodes.add(i)
        visited = set()
        memo = {}
        def dfs(node):
            if node in memo:
                return memo[node]
            if node in visited:
                memo[node] = False
                return False
            visited.add(node)
            for nnode in graph[node]:
                res = dfs(nnode)
                if not res:
                    memo[node] = False
                    return False
            memo[node] = True
            return True
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans
            
            
            