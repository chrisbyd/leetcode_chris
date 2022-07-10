from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        sign, i, j = 1, 0, 0
        if abs(len(positives) - len(negatives)) > 1:
            return False
        ans = []
        while i != len(positives) or j != len(negatives):
            if sign == 1:
                ans.append(positives[i])
                i += 1
            else:
                ans.append(negatives[j])
                j += 1
            sign = 1 - sign
        return ans



sol = Solution()
nums = [3,1,-2,-5,2,-4]
nums = [1, -1]
res = sol.rearrangeArray(nums)
print(res)