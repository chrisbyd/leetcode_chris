from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        n = len(graph)
        ans = []
        def dfs(cnode, path):
            if cnode == n-1:
                ans.append(path )
            else:
                visited.add(cnode)
                for nnode in graph[cnode]:
                    dfs(nnode, path + [nnode])
        dfs(0, [0])
        return ans
            
        