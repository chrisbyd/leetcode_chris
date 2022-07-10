from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = arr2[:]
        for num in arr2:
            arr1.remove(num)
        new_ans = []
        for num in arr1:
            if num in arr2:
                index = ans.index(num)
                ans.insert(index, num)
            else:
                new_ans.append(num)
        
        new_ans.sort()
        ans.extend(new_ans)
        return ans

sol = Solution()
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
res = sol.relativeSortArray(arr1, arr2)
print(res)



      

        