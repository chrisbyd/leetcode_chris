from typing import List

#### tle error

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        ans = 0
        for i in range(len(height)):
            right_max = 0 if i == len(height) -1 else max(height[i+1:])
            water = max(0,  min(left_max, right_max) - height[i])
            ans += water
            left_max = max(left_max, height[i])
        return ans

            
        

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
res = sol.trap(height)
print(res)


# accepted version without
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, length = 0,  len(height) 
        ans = 0
        right_max = [0 for i in range(length)]
        res = height[-1]
        for i in range(length-2,  -1, -1):
            right_max[i] = max(res , height[i+1])
            res = max(res , height[i+1])
            
        for i in range(len(height)):
            r_max = right_max[i]
            water = max(0,  min(left_max, r_max) - height[i])
            ans += water
            left_max = max(left_max, height[i])
        return ans


### two pointer solution
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, length = 0,  len(height) 
        ans = 0
        right_max = [0 for i in range(length)]
        res = height[-1]
        for i in range(length-2,  -1, -1):
            right_max[i] = max(res , height[i+1])
            res = max(res , height[i+1])
            
        for i in range(len(height)):
            r_max = right_max[i]
            water = max(0,  min(left_max, r_max) - height[i])
            ans += water
            left_max = max(left_max, height[i])
        return ans
