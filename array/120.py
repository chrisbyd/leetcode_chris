from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def miniIndex(triangle, index):
            num_layers = len(triangle)
         
            if len(triangle) == 0:
                return 0
            elif  len(triangle) == 1:
                return triangle[0][0]
            elif index == 0:
                return miniIndex(triangle[:num_layers-1], index) + triangle[-1][index]
            elif index == len(triangle[-1]) -1:
                return triangle[-1][index] +  miniIndex(triangle[:num_layers-1], index-1) 
            else: 
                return triangle[-1][index] + min(miniIndex(triangle[:num_layers-1], index), miniIndex(triangle[:num_layers - 1], index -1))

        if len(triangle) == 0:
            return 0
        else:
            res = []
            for index in range(len(triangle[-1])):
                res.append(miniIndex(triangle, index))
            return min(res)

class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        
        res = []
        for i in range(len(triangle)):
            res.append([])
            for index, j in enumerate(triangle[i]):
                if i == 0:
                    res[i].append(triangle[0][0])
                elif index == 0:
                    res[i].append(res[i-1][0] + triangle[i][0])
                elif index == len(triangle[i]) - 1:
                    res[i].append(res[i-1][-1] + triangle[i][-1])
                else:
                    res[i].append(min(res[i-1][index], res[i-1][index - 1]) + triangle[i][index] )
        return min(res[-1])




sol = Solution1()
tra = [[2],[3,4],[6,5,7],[4,1,8,3]]
res  = sol.minimumTotal(tra)
print(res)
                
                
            
tra = [[-10]]
res  = sol.minimumTotal(tra)
print(res)

