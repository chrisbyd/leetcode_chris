from typing import List
from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in allowedSwaps:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        def dfs(node, curlist):
            if node in visited:
                return curlist
            visited.add(node)
            curlist.append(node)
            for nnode in graph[node]:
                if nnode not in visited:
                    _ = dfs(nnode, curlist)
            return curlist
        
        connectedIndices = []
        for i, j in allowedSwaps:
            res = dfs(i, [])
            if res:
                connectedIndices.append(res)
        ans = 0
        totalIndices = set([i for i in range(len(source))])
        curIndices = set()
        for indices in connectedIndices:
            curIndices = curIndices | set(indices)
            s1 = sorted([source[idx] for idx in indices])
            s2 = sorted([target[idx]  for idx in indices])
            left, right = 0, 0
            res = 0
            while left < len(s1) and right < len(s2):
                if s1[left] < s2[right]:
                    left += 1
                elif s1[left] > s2[right]:
                    right += 1
                else:
                    left += 1
                    right += 1
                    res += 1
            ans += len(s2) - res

            
        leftIndices = totalIndices - curIndices
        for idx in leftIndices:
            ans += 1 if source[idx] != target[idx] else 0
        return ans

sol = Solution()
source = [2,3,1]
target = [1,2,2]
pairs = [[0,2],[1,2]]
source = [1,2,3,4]
target = [2,1,4,5]
pairs = [[0,1],[2,3]]
source = [18,67,10,36,17,62,38,78,52]
target = [3,4,99,36,26,58,29,33,74]
pairs = [[4,7],[3,1],[8,4],[5,6],[2,8],[0,7],[1,6],[3,7],[2,5],[3,0],[8,5],[2,1]
,[6,7],[5,1],[3,6],[4,0],[7,2],[2,6],[4,1],[3,2]
,[8,6],[8,0],[5,3],[1,0],[4,6],[8,7],[5,7],[3,8],[6,0],[8,1],[7,1],[5,0],[4,3],[0,2]]

res = sol.minimumHammingDistance(source, target,pairs)
print(res)