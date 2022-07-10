from typing import List, Optional

### tle because the bfs
from collections import deque, defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
     
    
        def bfs(node):
            visited = set() 
            visited.add(node)
            q = deque([node])
            visited
            depth = 0
            while q:
                depth += 1
                for _ in range(len(q)):
                    curnode = q.popleft()
                    for newNode in graph[curnode]:
                        if newNode not in visited:
                            q.append(newNode)
                            visited.add(newNode)
            return depth
        
        heights = []
        for i in range(n):
            height = bfs(i)
            heights.append(height)
        min_height = min(heights)
        res = []
        for i in range(n):
            if heights[i] == min_height:
                res.append(i)
        return res
                    


### tle because the bfs
from collections import deque, defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        if n == 1:
            return [0]
        leaves = [node for node in graph.keys() if len(graph[node]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leaf in leaves:
                print(leaf)
                print(graph)
                if len(graph[graph[leaf][0]]) == 2:
                    new_leaves.add(graph[leaf][0])
                graph[graph[leaf][0]].remove(leaf)
            
            leaves = new_leaves
        return leaves


n = 4
edges = [[1,0],[1,2],[1,3]]
sol = Solution()
res = sol.findMinHeightTrees(n, edges)
print(res)
    
