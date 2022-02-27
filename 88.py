from typing import List 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_nums = []
        i , j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                new_nums.append(nums1[i])
                i += 1
            else:
                new_nums.append(nums2[j])
                j += 1
        
        if i < m:
            new_nums.extend(nums1[i:m])
        if j < n:
            new_nums.extend(nums2[j:n])
        for index, item in enumerate(new_nums):
            nums1[index] = item



# nums1 = [1]
# nums2 = []
# m, n = 1, 0

# sol = Solution()
# res = sol.merge(nums1,m,nums2,n)
# print(nums1)


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n -1
        i ,j = m-1, n -1
        while j >=0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1 



nums1 = [0]
nums2 = [4]
m, n = 0, 1

sol = Solution1()
res = sol.merge(nums1,m,nums2,n)
print(nums1)