from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(c_list, depth, numbers):
            if depth == 0:
                if sum(c_list) == n:
                    res.append(c_list[:])
            else:
                for index, num in enumerate(numbers):
                    new_numbers = numbers[index +1 :]
                    c_list.append(num)
                    backtrack(c_list, depth -1, new_numbers)
                    c_list.remove(num)
               
        backtrack([], k, [i for i in range(1,10)])
        return res

sol = Solution()
k = 3
n = 9
res = sol.combinationSum3(k , n)
print(res)









        