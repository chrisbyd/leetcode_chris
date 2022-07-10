from typing import List



# accepted brutal force
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        ans = 0
        for i in range(lower, upper+1):
            hidden = True
            start = i
            for j in differences:
                if start + j > upper or start +j < lower:
                    hidden = False
                    break
                else:
                    start = start +j
            if hidden:
                ans += 1
        return ans
sol = Solution()
differences = [1,-3,4]
lower = 1
upper = 6
res = sol.numberOfArrays(differences, lower, upper)
print(res)
        
# an o(N) solution

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        new_array = []
        res = 0
        for num in differences:
            res += num
            new_array.append(res)
        ma, mi = max(new_array), min(new_array)
        ans = 0
        for i in range(lower, upper+1):
            if not(i + ma > upper or i + mi < lower):
                ans += 1
        return ans

sol = Solution()
differences = [1,-3,4]
lower = 1
upper = 6
res = sol.numberOfArrays(differences, lower, upper)
print(res)



