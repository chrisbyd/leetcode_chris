from typing import List

import bisect
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            find = False
            res = -1
            for i in range(len(nums2)):

                if find and nums2[i] > num:
                    res = nums2[i]
                    break
                elif nums2[i] == num:
                    find = True
            ans.append(res)
        return ans

sol = Solution()

nums1 = [4,1,2]
nums2 = [1,2,3,4]
res = sol.nextGreaterElement(nums1, nums2)
print(res)

from typing import List

import bisect
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hmap = {}
        # for idx, num in enumerate(nums1):
        #     hmap[num] = idx
        hmap = {n:i for i,n in enumerate(nums1)}
        ans = [-1 for _ in range(len(nums1))]
        
        for i, num in enumerate(nums2):
            if num in hmap:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > num:
                        ans[hmap[num]] = nums2[j]
                        break
        return ans

##with stack
        
from typing import List

import bisect
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums2index = { n:i for i, n in enumerate(nums1)}
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                if num in nums2index:
                    index = nums2index[num]
                    ans[index] = nums2[i]
            stack.append(nums2[i])
        return ans
                
            
                    
                    