from functools import lru_cache
from typing import List

### correct
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = set()
        graph = {}
        for flight in flights:
            graph[flight[0], flight[1]] = flight[-1]
        
        def dfs(c_position, c_price, hop):
            if c_position == dst:
                return c_price
            elif hop > k:
                return float('inf')
            elif hop <= k:
                ans = []
                visited.add(c_position)
                for i in range(n):
                    if (c_position, i) in graph and i not in visited:
                        ans.append(dfs(i, c_price + graph[c_position, i], hop+1))
                visited.remove(c_position)
                return min(ans) if ans else float('inf')
        res = dfs(src, 0, 0) 
        return res if res != float('inf') else -1

sol = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200], [0,2, 100]]
src = 0
dst = 3
k = 1
res = sol.findCheapestPrice(n, flights, src, dst, k)
print(res)




### with memorization
# This is the DFS solution
# with memo is wrong 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = set()
        graph = {}
        for flight in flights:
            graph[flight[0], flight[1]] = flight[-1]
        memo = {}
        def dfs(c_position, hop):
            print('The current position and hop is', c_position, hop)
            if (c_position, hop) in memo:
                return memo[c_position, hop] 
            if c_position == dst:
                res = 0
            elif hop > k:
                res = float('inf')
            elif hop <= k:
                ans = []
                visited.add(c_position)
                for i in range(n):
                    if (c_position, i) in graph and i not in visited:
                        ans.append(dfs(i, hop+1) +  graph[c_position, i])
                visited.remove(c_position)
            
                res = min(ans) if ans else float('inf')
            memo[c_position, hop] = res 
            return res
        res = dfs(src, 0) 
        return res if res != float('inf') else -1

sol = Solution()
n = 5
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,100],[2,3,200], [0,2, 100], [0, 4, 10], [4, 1, 20]]
flights = [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]]
src = 0
dst = 4
k = 3
res = sol.findCheapestPrice(n, flights, src, dst, k)
print(res)

# BFS solution 
import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fro, to, price in flights:
            graph[fro].append((to, price))
        pq = [(0, 0, src)]
        # store the minimum price for each node and possibe # of stops for 0..k
        minPrice = [[float('inf')] * (k+1)  for _ in range(n)]
        minPrice[src] = [0] * (k+1)
        while pq:
            curPrice, stops, curNode = heapq.heappop(pq)
            if curNode == dst:
                return curPrice
            
            if curPrice > minPrice[curNode][stops]:
                continue

            for to, cost in graph[curNode]:
                nextNumStops = stops if to == dst else stops + 1
                nextCost = cost + curPrice

                if nextNumStops <= k and nextCost < minPrice[to][nextNumStops]:
                    heapq.heappush(pq, (nextCost, nextNumStops, to))
                    minPrice[to][nextNumStops] = nextCost
        return -1

from collections import deque
#easy solution with simple bfs
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        minCost = [float('inf') for _ in range(n)]
        queue = deque([(src, 0)])
        stops = -1 
        while queue and stops < k:
            stops += 1
            length = len(queue)
            for i in range(length):
                node, cost = queue.popleft()
                for nextNode, nextCost in graph[node]:
                    if  nextCost + cost < minCost[nextNode]:
                        queue.append((nextNode, nextCost + cost))
                        minCost[nextNode] = nextCost + cost

        return minCost[dst] if minCost[dst] != float('inf') else -1

