from collections import defaultdict
from heapq import heappop, heappush
from typing import List
import sys
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,  w))
            graph[v].append((u,  w))
        sDist = [sys.maxsize] * (n + 1)
        sDist[n] = 0
        seen = set()
        heap = [(0, n)]
        while heap:
            distance, node = heappop(heap)
            if node not in seen:
                seen.add(node)
                sDist[node] = distance
                for nnode, dis in graph[node]:
                        nd  = distance + dis
                        if nd < sDist[nnode]:
                            sDist[nnode] = nd
                            heappush(heap, (sDist[nnode], nnode))
        @lru_cache(None)     
        def dp(node):
            if node == n:
                return 1
            else:
                ans = 0
                distance = sDist[node]
                for nnode, w in graph[node]:
                    if sDist[nnode] < distance:
                        ans += dp(nnode)
                return ans % (10 ** 9 + 7)
                    

        return dp(1)
                        
        
sol = Solution()
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
res = sol.countRestrictedPaths(n, edges)
print(res)