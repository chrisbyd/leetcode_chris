from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        inter = nums1 & nums2
        return list(inter)

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
res = sol.intersection(nums1, nums2)
print(res)