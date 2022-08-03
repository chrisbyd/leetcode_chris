#my solution with unionfind
from typing import List
class UnionFind(object):
    def __init__(self, n):
        self.storage = [i for i in range(n)]
    
    def root(self, a):
        if self.storage[a] == a:
            return a
        else:
            return self.root(self.storage[a])
    
    def height(self, a):
        def recur(a, height):
            if self.storage[a] == a:
                return height
            else:
                return recur(self.storage[a], height + 1)
        return recur(a, 1)
    
    def union(self, a, b):
        ra, ha = self.root(a), self.height(a)
        rb, hb = self.root(b), self.height(b)
        if ha < hb:
            self.storage[ra] = rb
        else:
            self.storage[rb] = ra
        
    def find(self, a, b):
        if self.root(a) == self.root(b):
            return True
        return False
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)
        ans = []
      
        for i in range(n):
            find = False
            for group in ans:
                if uf.find(i, group):
                    find = True
            if not find:
                ans.append(i)
        return len(ans)

sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
res = sol.findCircleNum(isConnected)
print(res)

### my solution with dfs

## dfs is much slower
from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(city):
            if city not in visited:
                visited.add(city)
                for ncity in graph[city]:
                    dfs(ncity)
            
        
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)
        ans = 0
        for c in range(n):
            if c not in visited:
                ans += 1
                dfs(c)
        return ans