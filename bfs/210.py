from typing import List
from collections import deque, defaultdict

from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {key: 0 for key in range(numCourses)}
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        startCourses = [key for key in indegree.keys() if indegree[key] == 0]
        print(startCourses)
        q = deque(startCourses)
        ans = []
        count = 0
        while q:
            course = q.popleft()
            count += 1
            ans.append(course)
            for ncourse in graph[course]:
                indegree[ncourse] -= 1
                if indegree[ncourse] == 0:
                    q.append(ncourse)
        if count == numCourses:
            return ans
        return []
            
        