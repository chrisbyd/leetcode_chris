from typing import List

# time limit exceeds due to the use of min
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        c_sum = arr[0] 
        prev = [[arr[0]]]
        for num in arr[1:]:
            new_prev = []
            for pre in prev:
                new_prev.append(pre + [num])
                curr = pre + [num]
                c_sum += min(curr)
            
            new_prev.append([num])
            prev = new_prev
            c_sum += num
        return c_sum

sol = Solution()
arr = [3,1,2,4]
res = sol.sumSubarrayMins(arr)
print(res)



# time limit exceeds due to the use of min
import math
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        c_sum = arr[0] 
        prev = [arr[0]]
        for num in arr[1:]:
            new_prev = []
            for pre in prev:
                if num < pre:
                    new_prev.append(num)
                    curr = num
                else:
                    new_prev.append(pre)
                    curr = pre
                c_sum += curr 
            new_prev.append(num)
            prev = new_prev
            c_sum += num
        return int(c_sum %  (math.pow(10,9) + 7))


sol = Solution()
arr = [3,1,2,4]

res = sol.sumSubarrayMins(arr)
print(res)


# still tle error trying to optimize it
# there exists an O(N) solution
import math
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pass
