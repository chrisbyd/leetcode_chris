from typing import List
###brutal force solution
####TLE 
# class Solution:
#     def maxSumMinProduct(self, nums: List[int]) -> int:
#         ans = -float('inf')
#         n = len(nums)
#         for i in range(n):
#             for j in range(i, n):
#                 nnums = nums[i: j + 1]
#                 ans = max(ans, min(nnums) * sum(nnums))
#         return ans % (10 ** 9 + 7)
    

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums.append(0) 
        prefix = [0] * (len(nums) + 1)
        stack = []
        res = 0
        
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
            while stack and num < nums[stack[-1]]:
                print(num, nums[stack[-1]], stack)
                minIndex = stack.pop()
                left = stack[-1] if stack else -1
                
                res = max(res, nums[minIndex] * (prefix[i] - prefix[left + 1]))
            stack.append(i)
            
        return res % (10 ** 9 + 7)

sol = Solution()
nums = [1,2,3,2]
res = sol.maxSumMinProduct(nums)
print(res)


# from typing import List
# ###brutal force solution
# class Solution:
#     def maxSumMinProduct(self, nums: List[int]) -> int:
#         ans = -float('inf')
#         n, stack = len(nums), []
#         psum = [0] * (n + 1)
       
#         for i in range(n):
#             psum[i+1] = psum[i] +nums[i]
#             minIndex = i
#             while stack and stack[-1][1] > nums[i]:
#                 minIndex, val = stack.pop()
#                 sumval = psum[i] - psum[minIndex ]
#                 ans = max(ans, val * sumval)
#             stack.append((minIndex, nums[i]))
#         while stack:
#             minindex, val = stack.pop()
#             sumval = psum[-1] - psum[minindex]
#             ans = max(ans, sumval * val)
#         return ans % (10 **9 + 7)