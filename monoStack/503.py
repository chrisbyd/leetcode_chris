from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, n  = [], len(nums)
        ans = []
        for i in range(n):
            find = False
            for nnum in (nums[i+1:] + nums[:i]):
                if nnum > nums[i]:
                    ans.append(nnum)
                    find = True
                    break
            if not find:
                ans.append(-1)
        return ans
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, n  = [], len(nums)
        ans = [-1 ] * n
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]
            stack.append(nums[i])
        
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]
            stack.append(nums[i])
            
        return ans
            
