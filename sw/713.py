from typing import List
from collections import defaultdict
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prep, dmap = 1, defaultdict(int)
        start = 0
        ans = 0
        for i in range(len(nums)):
            prep *= nums[i]
            print(prep)
            while prep >= k:
                print(start, prep, i)
                if start > i:
                    break
                prep = prep // nums[start]
                print(prep)
                start += 1
                
            ans += i - start + 1
        return ans

sol = Solution()
nums = [1,1,1]
k = 1
res = sol.numSubarrayProductLessThanK(nums, k)
print(res)

             
            
        
        