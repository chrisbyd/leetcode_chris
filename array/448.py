from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        ans = []
        for i in range(1, len(nums)+1):
            if i not in a:
                ans.append(i)
        return ans
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
res = sol.findDisappearedNumbers(nums)
print(res)