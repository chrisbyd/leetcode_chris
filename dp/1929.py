from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.extend(nums[:])
        ans.extend(nums[:])
        return ans

sol = Solution()
nums = [1,2,1]
res = sol.getConcatenation(nums)
print(res)