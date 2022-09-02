from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left, right = 0, 0
        middle = (m + n) // 2
        count = -1
        pre, cur = 0, 0
        while left < m and right < n and count < middle:
            if nums1[left] <= nums2[right]:
                pre = cur
                cur = nums1[left]
                left += 1
            else:
                pre = cur
                cur = nums2[right]
                right += 1
            count += 1
        
        nums = nums1[left:] if left < m else nums2[right:]
        i = 0
        while count < middle:
            pre = cur
            cur =nums[i]
            i += 1
            count += 1

        if (m+ n) % 2 == 0: 
            return (pre + cur) / 2
        else:
            return cur
     
sol = Solution()
nums1 = [1,3]
nums2 = [2]
res = sol.findMedianSortedArrays(nums1, nums2)
print(res)