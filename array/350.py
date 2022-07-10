from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_s, nums_l = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        res = []
        for num in nums_s:
            if num in nums_l:
                nums_l.remove(num)
                res.append(num)
        return res
        
nums1 = [1,1]
nums2 = [1,4,9,8,4]
sol = Solution()
res = sol.intersect(nums1, nums2)
print(res)