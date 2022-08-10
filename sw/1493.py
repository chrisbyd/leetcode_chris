from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        intervals = []
        prev = -1
        if sum(nums) == len(nums):
            return len(nums) -1
        for end, num in enumerate(nums):
            if num != 1 :
                if end != 0:
                    intervals.append([prev + 1 , end])
                prev = end
        if num == 1:
            intervals.append([prev+ 1, end + 1])
        n = len(intervals)
        previ, prevj = intervals[0]
        ans = prevj - previ
        for i in range(1, n):
            curi, curj = intervals[i]
            if curi - prevj == 1:
                ans = max(ans,  curj - previ -1)
            else:
                ans = max(ans, curj - curi, prevj - previ)
            previ, prevj = curi, curj
        return ans
                
            
        
                
                
            
        
                
                
sol = Solution()
nums = [1,1,1]
res = sol.longestSubarray(nums)
print(res)