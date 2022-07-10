from typing import List
import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
            if len(dp) == 3:
                return True
        return False

nums = [2,1,5,0,4,6]
#nums = [5,4,3,2,1]
sol = Solution()
res = sol.increasingTriplet(nums)
print(res)

import sys
class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minmum, medium = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= minmum:
                minmum = num
            elif num <= medium:
                medium = num
            else:
                return True
        return False


nums = [1,1,1,1,1]
#nums = [5,4,3,2,1]
sol = Solution1()
res = sol.increasingTriplet(nums)
print(res)