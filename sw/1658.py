from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        tsum = sum(nums)
        target = tsum - x
        if target < 0: return -1
        if target == 0: return len(nums)
        start, cumsum, ans = 0, 0, 0
        for end, num in enumerate(nums):
            cumsum += num
            while cumsum >  target:
                cumsum -= nums[start]
                start += 1
            if cumsum == target :
                ans = max(ans , end - start + 1)
        return len(nums) - ans if ans !=0 else -1
        