from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cum = 0
        for num in  nums:
            cum += num
            ans.append(cum)
        return ans