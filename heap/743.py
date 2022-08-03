from typing import List


from typing import List

## this is rong
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append([v, time])
        ans = {}
        def dfs(node, time):
            if node not in ans:
                ans[node] = time
                for nnode, t in graph[node]:
                    dfs(nnode, time + t)
        dfs(k, 0)
        if len(ans.keys()) == n:
            return max(ans.values())
        return -1
        
### correct answer with bfs and heap
from typing import List
from collections import defaultdict
from heapq import heappush, heappop 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append([v, time])
        ans = {}
        while heap:
            t, node = heappop(heap)
            if node not in ans:
                ans[node] = t
                for nnode, t1 in graph[node]:
                    if nnode not in ans:
                        heappush(heap, (t+ t1, nnode))
        if len(ans.keys()) == n:
            return max(ans.values())
        return -1
                    
            
            
        