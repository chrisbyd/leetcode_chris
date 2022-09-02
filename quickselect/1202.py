from typing import List
from typing import List
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        
        def dfs(node, curIns):
            if node in visited:
                return curIns
            visited.add(node)
            curIns.append(node)
            for nnode in graph[node]:
                if nnode not in visited:
                    dfs(nnode, curIns)
            return curIns
        
        connectedIndices = []
        for i, j in pairs:
            res = dfs(i, [])
            if res:
                connectedIndices.append(res)
        ans = [0] * len(s)
        for indices in connectedIndices:
            toSort = [s[idx] for idx in indices]
            toSort = sorted(toSort)
            cur = 0
            for idx in sorted(indices):
                ans[idx] = toSort[cur]
                cur += 1
        for i in range(len(s)):
            if ans[i] == 0:
                ans[i] = s[i]
        return "".join(ans) 
sol = Solution()
s = 'dcab'
pairs =[[0,3],[1,2],[0,2]]
res = sol.smallestStringWithSwaps(s, pairs)
print(res)