from typing import List, Optional

from collections import defaultdict



##### time limit error
class Solution:
   
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        all_visited = set()
        memo = {}
        for x, y in prerequisites:
            graph[y].append(x)
            
        def dfs(node, visited):
            print(node)
            if node in visited: 
                memo[node] = True
                return True
            all_visited.add(node)
            visited.add(node)
         
            for nextNode in graph[node]:
                if not dfs(nextNode, visited):
                    return True
            visited.remove(node)
            return False
        
        for i in range(numCourses):
            if i not in all_visited:
                if dfs(i, set()):
                    return False
        return True


# sol = Solution()
# n = 5
# prerequisites = [[1,0], [4,3], [3,4]]
# n = 2
# prerequisites = [[1,0],[0,1]]
# res = sol.canFinish(n, prerequisites)
# print(res)


# from collections import deque
##topological sort algorithm
# class Solution:
#        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = defaultdict(list)
#         indegree = defaultdict(int)

#         for x, y in prerequisites:
#             graph[y].append(x)
#             indegree[x] += 1
        
#         start_courses = [key for key in range(numCourses) if indegree[key] == 0]
#         q = deque(start_courses)
#         count = 0
#         while q:
#             course = q.popleft()
#             count += 1
#             for nextCourse in graph[course]:
#                 indegree[nextCourse] -= 1
#                 if indegree[nextCourse] == 0:
#                     q.append(nextCourse)
#         if count == numCourses:
#             return True
#         return False


            

# sol = Solution()
# n = 4
# prerequisites = [[1,0],[2,1],[3,2]]
# res = sol.canFinish(n, prerequisites)
# print(res)



#### with memorization, it passes
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visitSet = set()
        memo = {}
        def dfs(crs):
            if crs in memo:
                return memo[crs]
            if crs in visitSet:
                memo[crs] = False
                return memo[crs]
            if preMap[crs] == []:
                memo[crs] = True
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    memo[crs] = False
                    return False
            visitSet.remove(crs)
            memo[crs] = True
          #  preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                    return False
       
        return True

        
n = 100
prerequisites = [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],[11,9],[11,10],[12,10]
,[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],
[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30]
,[32,30],[32,31],[33,31],[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],[41,39],[41,40]
,[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50]
,[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60]
,[62,61],[63,61],[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],[71,69],[71,70],[72,70],[72,71],[73,71],
[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83]
,[85,83],[85,84],[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97]
,[99,97]]

sol = Solution()

res = sol.canFinish(n, prerequisites)
print(res)
