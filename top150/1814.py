from collections import defaultdict
from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(num):
            digits = []
            while num:
                digit = num % 10
                digits.append(digit)
                num = num // 10

            ans = 0
            for digit in digits: 
                ans = ans * 10 + digit
            return ans
        cmap = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            ele = nums[i] - reverse(nums[i])
            ans += cmap[ele]
            cmap[ele] += 1
        return ans % (10 **9 +7)

sol = Solution()
nums = [42,11,1,97]
res = sol.countNicePairs(nums)
print(res)