from typing import List



#Kadane Algorithm


#prefix sum and mono queue
from collections import deque

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0]

        # compute p[j] = sum(B[:j]) for the fiexed array B = A + A
        for _ in range(2):
            for x in nums:
                psum.append(psum[-1] + x)
        
        ans = nums[0]
        Deque = deque([0])
        for j in range(1, len(psum)):
            if Deque[0] < j - n:
                Deque.popleft()

            ans = max(ans, psum[j] - psum[Deque[0]])

            while Deque and psum[j] <= psum[Deque[-1]]:
                Deque.pop()
            Deque.append(j)
        
        return ans





#### Kadane"s algorithm (Sign variant) 
### Two possibilities
#1: when maximum subarray sum lies in between the array
#2: when the first and the last element of the array contributes to the subarray sum

# def kadanes(nums):
#             ans = - float("inf")
#             sum_so_far = 0
#             for num in nums:
#                 sum_so_far += num
#                 ans = max(ans, sum_so_far)
#                 sum_so_far = 0 if sum_so_far < 0 else sum_so_far
#             return ans

# nums = [2,-1,3,2,4]
# print(kadanes(nums))

### This solution is pretty nice 啊
#1: when maximum subarray sum lies in between the array
#2: when the first and the last element of the array contributes to the subarray sum
# so for the second case 
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadanes(nums):
            ans = - float("inf")
            sum_so_far = 0
            for num in nums:
                sum_so_far += num
                ans = max(ans, sum_so_far)
                sum_so_far = 0 if sum_so_far < 0 else sum_so_far
            return ans
        
        ### case 1 
        max_sub_sum_1 = kadanes(nums)
        max_sub_sum_2 = sum(nums) + kadanes([-i for i in nums])
        ans = max(max_sub_sum_1, max_sub_sum_2)
        return ans

sol = Solution()
nums = [2, -1, -3, -4, 4]
res = sol.maxSubarraySumCircular(nums)
print(res)






















        



        