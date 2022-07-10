from typing import List, Optional

from collections import defaultdict



##### time limit error
class Solution:
    all_visited = set()
    memo = {}
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[y].append(x)
            
        def dfs(node, visited):
            if node in self.memo:
                return self.memo[node]

            if node in visited: 
                self.memo[node] = True
                return True
            
            self.all_visited.add(node)
            visited.add(node)
            ans = False
            for nextNode in graph[node]:
                ans = ans or dfs(nextNode, visited)
            visited.remove(node)
            return ans
        
        for i in range(numCourses):
            if i not in self.all_visited:
                if dfs(i, set()):
                    return False
        return True


sol = Solution()
n = 5
prerequisites = 
res = sol.canFinish(n, prerequisites)
print(res)