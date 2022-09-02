from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def subsets(index, ans ):
            if index == len(nums):
                res.append(ans)
            else:
                subsets(index + 1, ans ^ nums[index])
                subsets(index +1 , ans)
        subsets(0, 0)
        return sum(res)
        