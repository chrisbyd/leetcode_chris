from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, left, n, cursum = 0, 0, len(nums), 0
        nSet = set()
        for right, num in enumerate(nums):
            if num not in nSet:
                nSet.add(num)
                cursum += num
                ans = max(ans, cursum)
            else:
                while left < right and num in nSet:
                    cursum -= nums[left]
                    nSet.remove(nums[left])
                    left += 1
                cursum += num
                nSet.add(num)
        return ans