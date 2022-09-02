from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for nl in nums:
            s = set(nl) & s
        s = sorted(list(s))
        return s
            