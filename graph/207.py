from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for prev, nextc in prerequisites:
            graph[prev].append(nextc)
            degree[nextc] += 1
        
        def findloop(start, curnode, encounter):
            if start ==  curnode and encounter != 0:
                return True
           
            for nnode in graph[curnode]:
                if findloop(start, nnode, encounter + 1):
                    return True
            return False
   
        for node in range(numCourses):
         
            if findloop(node, node, 0):
                return False
        return True

sol = Solution()
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
res = sol.canFinish(numCourses, prerequisites)
print(res)