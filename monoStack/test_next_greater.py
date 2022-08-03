from typing import List

class Solution:
    def nextGreaterElement(self, nums):
        n = len(nums)
        ans = [0 for i in range(n)]
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return ans

sol = Solution()
nums = [2,1,2,4,3]
res = sol.nextGreaterElement(nums)
print(res) 

class Solution1:
    def daysNeedToWait(self, temperature: List) -> List:
        n = len(temperature)
        ans = [0 for i in range(n)]
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= temperature[i]:
                stack.pop()
            ans[i] = stack[-1][1] - i if stack else 0
            stack.append((temperature[i], i))
        return ans

sol = Solution1()
T = [73, 74, 75, 71, 69, 72, 76, 73]
res = sol.daysNeedToWait(T)
print(res) 