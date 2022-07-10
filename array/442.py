from typing import List
import collections
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hmap = collections.defaultdict(int)
        for num in nums:
            hmap[num] += 1
        ans = []
        for key in hmap.keys():
            if hmap[key] == 2:
                ans.append(key)
        return ans

sol = Solution()
nums = [4,3,2,7,8,2,3,1]
res = sol.findDuplicates(nums)
print(res)

        