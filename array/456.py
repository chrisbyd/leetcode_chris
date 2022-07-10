from typing import List

# a naive approach
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pass 

import bisect
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_array = [0 for i in range(len(nums))]
        min_array[0] = nums[0]
        min_ele = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < min_ele:
                min_ele = nums[i]
            min_array[i] = min_ele
        right_array = [nums[-1]]
        for i in range(len(nums) -2, 0, -1):
            r_index = bisect.bisect_left(right_array, nums[i])
            if r_index == 0:
                right_array.insert(r_index, nums[i])
                continue
            elif right_array[r_index - 1] > min_array[i-1] and right_array[r_index - 1] < nums[i]:
                return True
            right_array.insert(r_index, nums[i])
        
        return False

sol  = Solution()
nums = [1,2,3,4]
nums = [-1,3,2,0]
res = sol.find132pattern(nums)
print(res)

import collections
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ans=False
        stack=collections.deque()
        n=len(nums)
        minLeft=[float('inf') for i in range(n)]
        minLeft[0]=nums[0]
        for i in range(1,n):
            minLeft[i]=min(minLeft[i-1],nums[i])
        for j in range(n-1,-1,-1):
            if nums[j]>minLeft[j]:
                while stack and stack[-1]<=minLeft[j]:
                    stack.pop()
                if stack and stack[-1]<nums[j]:
                    ans=True
                    break
                else:
                    stack.append(nums[j])
        return ans


            




            










        










        