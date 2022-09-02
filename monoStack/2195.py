from typing import List
###tle
# class Solution:
#     def minimalKSum(self, nums: List[int], k: int) -> int:
#         nums = set(nums)
#         cur = 1
#         ans = 0
#         while k != 0:
#             if cur not in nums:
#                 ans += cur
#                 k -= 1
#             cur += 1
#         return ans
        
        
from typing import List
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = ( 1 + k) /2 * k
        nums.sort()
        maximum = k+1 
        numset = set(nums)
        for num in numset:
            if num <= k:
                ans -= num
                while maximum in numset:
                    maximum += 1
            
                ans += maximum 
                maximum += 1
        return int(ans)
        
sol = Solution()
nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
k = 35
res = sol.minimalKSum(nums, k)
print(res)