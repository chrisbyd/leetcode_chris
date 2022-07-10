from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = 0
        memo = set()
        for num in nums:
            if num not in memo:
                count += 1
                memo.add(num)
                if count == 3:
                    return num
        return max(nums)
        
sol = Solution() 
nums = [3,2,1]
res = sol.thirdMax(nums)
print(res)
