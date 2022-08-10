from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum, ans = sum(nums[: k]), []
        ans =  float(total_sum / k)
        for r in range(k, len(nums)):
            total_sum += nums[r]
            total_sum -= nums[r- k]
            ans = max(ans, float(total_sum / k))
        return ans
    
        
        