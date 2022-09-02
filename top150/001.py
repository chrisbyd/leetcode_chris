from typing import List
import bisect
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = defaultdict(list)
        for idx, num in enumerate(nums):
            numdict[num].append(idx)

        for idx, num in enumerate(nums):
            remain = target - num
            if remain != num:
                if numdict[remain]:
                    return [idx, numdict[remain][0]]
            else:
                if len(numdict[remain]) == 2:
                    return [idx, numdict[remain][1]]
        return False
            
        
sol = Solution()
nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
res = sol.twoSum(nums, target)
print(res)