from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        presum = [0]
        cum = 0
        ans = []
        for num in arr:
            cum = cum ^ num
            presum.append(cum)
        print(presum)
        for x, y in queries:
            res = presum[y+1] ^ presum[x]
            ans.append(res)
        return ans
            
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
sol = Solution()
res = sol.xorQueries(arr , queries)
print(res)