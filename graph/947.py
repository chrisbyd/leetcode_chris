from heapq import heappop, heappush


class UF:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
    
    def root(self, node):
        if self.roots[node] == node:
            return node
        else:
            return self.root(self.roots[node])
    
    def height(self, node):
        def dp(node):
            if self.roots[node] == node:
                return 1
            else:
                return 1 + dp(self.roots[node])
        return dp(node)
    
    def union(self, a, b):
        ra,  ha = self.root(a), self.height(a)
        rb, hb = self.root(b), self.height(b)
        if a < b:
            self.roots[ra] = rb
        else:
            self.roots[rb] = ra

    
    def find(self, a, b):
        if self.root(a) == self.root(b):
            return True
        return False
    
    def numberOfRoots(self):
        roots = set()
        n = len(self.roots)
        for i in range(n):
            roots.add(self.root(i))
        return len(roots)
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return n - uf.numberOfRoots()

            
        