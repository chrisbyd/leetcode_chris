from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num2index = {}
        n = len(nums2)
        for i, num in enumerate(nums2):
            num2index[num] = i
        ans2 = [-1] * len(nums2)
        for i in range(n-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                ans2[i] = stack[-1]
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            index = num2index[num]
            ans.append(ans2[index])
        return ans