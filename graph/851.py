from typing import List
from typing import List
from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        memo = {}
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
            
        def dfs(node):
            if node in memo:
                return memo[node]
            
            if not graph[node]:
                memo[node] = [node, quiet[node]]
                return memo[node]
            
            ans = []
            for nnode in graph[node]:
                ans.append(dfs(nnode))
            res = min(ans, key = lambda x: x[1])
            
            ans = min([res] + [[node, quiet[node]]], key = lambda x : x[1])
            memo[node] = ans
            return ans
        ans = []
        for person in range(len(quiet)):
            p, q = dfs(person)
            ans.append(p)
        return ans
                
        
sol = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
richer = [[0,1],[1,2]]
quiet = [1,0,2]
res = sol.loudAndRich(richer, quiet)
print(res)

from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        memo = {}
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        answer = [None] * len(quiet)
        def dfs(node):
            if answer[node] is None:
                answer[node] = node
                for nnode in graph[node]:
                    cand = dfs(nnode)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]
        return map(dfs, range(len(quiet)))
            
            
            
        

