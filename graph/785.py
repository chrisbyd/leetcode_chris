from collections import deque
from typing import List

#####when adding to the queue, remember to add it to the visited  588ms
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        n = len(graph)
        colors = [-1] * n
        for node in range(n):
            if node not in visited:
                q = deque([node])
                while q:
                    node = q.popleft()
                    visited.add(node)
                    color = 1 if colors[node] == -1 else colors[node]
                    colors[node] = color
                    for nnode in graph[node]:
                        if colors[nnode] == color: 
                            return False
                        else:
                            colors[nnode] = 1 - color
                        if nnode not in visited:
                            q.append(nnode)
        return True
                    
#### in this version, it is much faster  196ms
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        n = len(graph)
        colors = [-1] * n
        for node in range(n):
            if node not in visited:
                q = deque([node])
                while q:
                    node = q.popleft()
                    visited.add(node)
                    color = 1 if colors[node] == -1 else colors[node]
                    colors[node] = color
                    for nnode in graph[node]:
                        if colors[nnode] == color: 
                            return False
                        else:
                            colors[nnode] = 1 - color
                            
                        if nnode not in visited:
                            visited.add(nnode)
                            q.append(nnode)
        return True
                    
        