from typing import List
from collections import defaultdict

### Floyd-Warshall algorithm
class Solution(object):
    def findTheCity(self, n, edges, t):
        dist = defaultdict(lambda : float('inf'))
        for u, v, w in edges:
            dist[u, v] = w
            dist[v, u] = w
        for i in range(n):
            dist[i,i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i,j] = min(dist[i,j], dist[i,k] + dist[k,j])
        
        ans = -1
        prev = n+1
        
        for i in range(n):
            res = 0
            for j in range(n):
                res += 1 if dist[i,j] <= t else 0
            if res <= prev:
                ans = i
                prev = res
        return ans
                
                