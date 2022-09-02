from typing import List
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for idx, (a, b ) in enumerate(edges):
            graph[a].append((b, succProb[idx]))
            graph[b].append((a, succProb[idx]))
        dist = [float('inf') for i in range(n)]
        dist[start] = 1
        heap = [(-1.0, start)]
        visited = set()
        while heap:
            prob, node = heappop(heap)
            if node in visited:
                continue
            dist[node] = - prob
            visited.add(node)
            for nnode, nprob in graph[node]:
                if nnode not in visited:
                    thisprob = min(prob * nprob,  dist[nnode])
                    heappush(heap, (thisprob, nnode ))
        return  dist[end]
sol =  Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succ = [0.5,0.5,0.2]
s = 0
e = 2
res = sol.maxProbability(n, edges, succ, s, e)
print(res)