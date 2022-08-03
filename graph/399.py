from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx , (x, y) in enumerate(equations):
            graph[x] .append([y, values[idx]])
            graph[y].append([x, 1 / values[idx]])
            # graph[x, x] = 1.0
            # graph[y, y] = 1.0
      
        def find(this, target, value):
            visited[this] = True
            if this == target:
                return value
            else:
                for nnode, val in graph[this]:
                    if nnode not in visited:
                        res =  find(nnode, target, value * val)
                        if res != - 1:
                            return res
                return - 1
        ans = []
        for start, target in queries:
            visited = {}
            if start not in graph or target not in graph:
                ans.append(-1.0)
            else:
                ans.append(find(start, target, 1.0))
        return ans
sol = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
res = sol.calcEquation(equations, values, queries)
print(res)