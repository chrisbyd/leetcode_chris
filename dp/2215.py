from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = []
        res = []
        for num in nums1:
            if num not in nums2:
                res.append(num)
        ans.append(res)
        res = []
        for num in nums2:
            if num not in nums1:
                res.append(num)

        ans.append(res)
        return ans

sol = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
res = sol.findDifference(nums1, nums2)
print(res)
        