from re import S
from typing import List

import collections
#Graph + DFS
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(float)
        all_vertices = set()
        for idx, (x, y) in enumerate(equations):
            all_vertices.add(equations[idx][0])
            all_vertices.add(equations[idx][1])
            graph[x, y] = values[idx]
            graph[y ,x] = 1 / values[idx]
        for vertice in all_vertices:
            graph[vertice,vertice] = 1.0
     
        def dfs(x, target,visited ,value):
            if x ==  target:
                return value
            else:
                value_to_return = -1.0
                for n_v in all_vertices:
                    if not visited[x,n_v] and graph[x,n_v] != 0.0:
                        visited[x,n_v] = 1 
                        
                        cur = dfs(n_v, target, visited, value* graph[x,n_v])
                        if cur != -1.0:
                            value_to_return = cur
                return value_to_return
        ans = []
        for q_x, q_y in queries:
            if q_x not in all_vertices:
                ans.append(-1.0)
            else:
                ans.append(dfs(q_x, q_y, collections.defaultdict(int), value= 1.0))
        return ans

sol = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
queries = [["a","c"]]
res = sol.calcEquation(equations, values, queries)
print(res)



# Solution 2  UNion Find algorithm
class UnionFind:
    def __init__(self, vertices) -> None:
        self.parents = [i for i in range(len(vertices))]
        self.values = [1 for i in range(len(vertices))]
        self.vertices = vertices
    
    def root(self, index):
        if self.parents[index] == index:
            return index
        else:
            return self.root(self.parents[index])
    
    def get_value_to_root(self, index):
        if self.parents[index] == index:
            return self.values[index]
    
        return self.values[index] * self.get_value_to_root(self.parents[index])

    def union(self, x, y, value):
        if x not in self.vertices or y not in self.vertices:
            return False
        idx_x = self.vertices.index(x)
        idx_y = self.vertices.index(y)
        root_x = self.root(idx_x)
        root_y = self.root(idx_y)
 
        self.parents[root_x] = root_y
        self.values[root_x] = self.get_value_to_root(idx_y) * value / self.get_value_to_root(idx_x)
        return True

    
    def find(self, x, y):
        if x not in self.vertices or y not in self.vertices:
            return -1.0
        idx_x = self.vertices.index(x)
        idx_y = self.vertices.index(y)
        if self.root(idx_x) != self.root(idx_y):
            return -1.0
        else:
           
            x_to_root = self.get_value_to_root(idx_x)
            y_to_root = self.get_value_to_root(idx_y)
            ans = x_to_root / y_to_root
          
            return ans

 

class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vertices = []
        for eq in equations:
            vertices.extend(eq)
        vertices = list(set(vertices))
        unionFind = UnionFind(vertices)
   
        for idx, (x, y) in enumerate(equations):
            unionFind.union(x,y, values[idx])
 

        res = []
        for x, y in queries:
            res.append(unionFind.find(x,y))
        return res

        
        
        
        

sol = Solution1()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
res = sol.calcEquation(equations, values, queries)
print(res)




### another graph-based solution
class Solution2:
    def find(self, graph, start, end, visited, value):
        if start == end:
            return value
        else:
            visited[start] = 1
            ans = -1
            for p, v in graph[start]:
                if not visited[p]:
                    cur_ans = self.find(graph, p, end, visited, value * v)
                    if cur_ans != -1:
                        ans = cur_ans
            return ans


    def search(self, graph, query):
        start, end = query[0], query[1]
        if start not in graph or end not in graph:
            return -1.0
        visited = collections.defaultdict(int)
        return self.find(graph, start, end, visited, 1)

        

    def calcEquation(self, equations, values, queries):
        res, graph = [], collections.defaultdict(list)
        for eq, value in zip(equations, values):
            graph[eq[0]].append((eq[1], value))
            graph[eq[1]].append((eq[0], 1/ value))
        for query in queries:
            res.append(self.search(graph, query))
        return res


        
        



sol = Solution2()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
res = sol.calcEquation(equations, values, queries)
print(res)


