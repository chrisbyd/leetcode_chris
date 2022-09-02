
from typing import List
### TLE because of the sum I guess
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, n = [], len(arr)
        ans = 0
        for i in range(n):
            count = 0
            
            while stack and stack[-1] > arr[i]:
                stack.pop()
                count += 1
            while count >= 0:
                stack.append(arr[i])
                count -= 1
            ans += sum(stack)
        return ans % (10 ** 9 +7)

### optimized version

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, n = [], len(arr)
        ans = 0
        res =0
        for i in range(n):
            count = 0

            while stack and stack[-1] > arr[i]:
                res -= stack.pop()
                count += 1
            while count >= 0:
                stack.append(arr[i])
                res += arr[i]
                count -= 1
            ans += res
        return ans % (10 ** 9 +7)
            
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, n = [], len(arr)
        ans = 0
        res =0
        for i in range(n):
            count = 0
            iindex = i
            while stack and stack[-1][1] >= arr[i]:
                index, val = stack.pop()
                res -= ((iindex - index) * val)
                iindex = index 
                count = (i - index)
            stack.append((iindex, arr[i]))
            res += arr[i] * (count + 1)
                
            ans += res
        return ans % (10 ** 9 +7)
            