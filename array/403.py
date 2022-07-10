from typing import List
import collections
# naive solution with O(N^2)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = collections.defaultdict(set)
        dp[0].add(1)
        for i in range(1, len(stones)):
            if i == 1 :
                if stones[i] != 1:
                    return False
                else:
                    dp[i].add(1)
            for j in range(1, i):
                jump = stones[i] - stones[j]
                if jump + 1 in dp[j] or jump in dp[j] or jump - 1 in dp[j]:
                    dp[i].add(jump)
       
        return False if len(dp[len(stones)-1]) == 0 else  True




sol = Solution()
stones = [0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]
res = sol.canCross(stones)
print(res)

        
# a better follow up question 
# DFS + memo
import collections

class Solution1:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        visited = collections.defaultdict(int)
        
        if stones[1] != 1:
            return False

        def dfs(current_location, jump):

            if current_location == stones[-1]:
                return True
            elif visited[current_location, jump] != 0:
                if visited[current_location, jump] == 1:
                    return False
                else:
                    return True
            for j in range(max(jump-1, 1), jump + 2):
                if (current_location + j) in stone_set :
                    if dfs(current_location + j, j):
                        visited[current_location, jump] = 2
                        return True
            visited[current_location, jump] = 1
            return False

        return dfs(1, 1)
    

sol = Solution1()
stones = [0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]
stones = [0,1,3,5,6,8,12,17]
stones = [0,2,4,5,6,8,9,11,14,17,18,19,20,22,23,24,25,27,30]
res = sol.canCross(stones)
print(res)



class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        visited = collections.defaultdict(int)
        
        if  stones[1] != 1:
            return False

        def dfs(current_location, jump):

            if current_location == stones[-1]:
                return True
        
            for j in range(max(jump-1, 1), jump + 2):
                if (current_location + j) in stone_set :
                    if dfs(current_location + j, j):

                        return True
            return False

        return dfs(1, 1)

sol = Solution2()
stones = [0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]
stones = [0,1,3,5,6,8,12,17]
stones = [0,2,4,5,6,8,9,11,14,17,18,19,20,22,23,24,25,27,30]
res = sol.canCross(stones)
print(res)