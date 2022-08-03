from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        pass
       

sol = Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
res = sol.possibleBipartition(n, dislikes)
print(res)


from typing import List
from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i: [] for i in range(1, n+1)}
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        visited = {} 
        colors = [-1 for i in range(n+1)]
        for i in range(1, n+1):
            if i not in visited:
                q = deque([i])
                while q:
                    node = q.popleft()
                    visited[node] = True
                    color = colors[node]
                    if color == -1:
                        colors[node] = 1
                    for nnode in graph[node]:
                        if colors[nnode] == colors[node]:
                            return False
                        else:
                            colors[nnode] = 1 - colors[node]
                        if nnode not in visited:
                            q.append(nnode)
        return True