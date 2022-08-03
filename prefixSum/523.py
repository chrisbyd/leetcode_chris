from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        current = 0
        for idx, num in enumerate(nums):
            current = (current + num) % k  
            if current not in remainder:
                remainder[current] = idx
            elif idx - remainder[current] >= 2:
                return True
        return False