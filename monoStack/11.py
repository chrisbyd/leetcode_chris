from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left <= right:
            water = min(height[right] , height[left]) * (right - left)
            ans = max(ans, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
                
                
            
        