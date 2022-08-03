from typing import List
import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = bisect.bisect_left(arr, x)
        
        right = left 
        left -= 1
  
        if right == len(arr):
            return arr[-k:]
        if left == -1:
            return arr[:k]
        
        while right - left < k + 1:
            print(left, right)
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            else:
                if abs(x - arr[left]) <= abs(x-arr[right]):
                    left -= 1
                else:
                    right += 1
            

        return arr[left+1: right]

sol = Solution()
arr = [1,2]
k = 1
x = 1
arr = [1,4,10]
k = 1
x = 4
res = sol.findClosestElements(arr, k, x)
print(res)