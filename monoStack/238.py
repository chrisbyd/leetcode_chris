from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        for num in reversed(nums):
            suffix.append(suffix[-1] * num)
        suffix = suffix[:: -1]
        ans = []
        for i in range(len(nums)):
            res = prefix[i] * suffix[i+1]
            ans.append(res)
        return ans
            