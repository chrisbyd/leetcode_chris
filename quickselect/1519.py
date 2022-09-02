from typing import List
from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        result = [0 for i in range(n)]
        visited = set() 
        def dfs(node):
            res = defaultdict(int)
            tem = [0 for i in range(26)]
            tem[ord(labels[node]) - 97] += 1
            visited.add(node)
            
            for nnode in graph[node]:
                if nnode not in visited:
                    tem1 = dfs(nnode)
                    tem = [a + b  for a, b in zip(tem, tem1)]
            result[node] = tem[ord(labels[node]) - 97]
            return tem
        dfs(0)
        return result
            
            
        