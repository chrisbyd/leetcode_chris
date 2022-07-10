from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 1:
            return len(nums)
        former = nums[0]
        max_conseq = 1
        cu_conseq = 1
        for i in range(1,len(nums)):
            if nums[i] - former == 1:
                cu_conseq += 1
                former = nums[i]
            elif nums[i] - former == 0:
                former = nums[i]
            else:
                former = nums[i]
                if cu_conseq > max_conseq:
                    max_conseq = cu_conseq
                cu_conseq = 1
        if cu_conseq > max_conseq:
                    max_conseq = cu_conseq
        return max_conseq

sol = Solution()
nums =  [1,2,0,1]
res = sol.longestConsecutive(nums)
print(res)
