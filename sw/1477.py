from typing import List
from heapq import heappop, heappush
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start, cumsum = 0, 0
        optimal = [float('inf')] * (len(arr) + 1)
        milen = float('inf')
        ans = float('inf')
        for end, num in enumerate(arr):
            cumsum += num
            while cumsum > target:
                cumsum -= arr[start]
                start += 1
            if cumsum == target:
                res = end - start + 1
                optimal[end+1] = min(optimal[end], res)
                if optimal[start] != float('inf'):
                    ans = min(optimal[start]+ res, ans)
            else:
                optimal[end + 1] = optimal[end]
            

        return ans if ans != float('inf') else -1
        

sol = Solution()
arr = [2,1,3,3,2,3,1]
target = 6
res = sol.minSumOfLengths(arr, target)
print(res)
