from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(k):
            removed = set(removable[:k])
            left, right = 0, 0
            n = len(p)
            for left in range(len(s)):
                if left in removed:
                    continue
                if s[left] == p[right]:
                    right += 1
                if right == n:
                    break
            return right == n
           

        left, right = 0, len(removable)
        res = 0
        while left <= right:
            middle = (left + right) // 2
         
            if isSubsequence(middle):
                left = middle + 1
                res = middle
            else:
                right = middle - 1
        return res

sol = Solution()
s = "abcbddddd"
p = "abcd"
remove = [3,2,1,4,5,6]
res = sol.maximumRemovals(s, p, remove)
print(res)

from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(k):
            removed = set(removable[:k])
            left, right = 0, 0
            n = len(p)
            for left in range(len(s)):
                if left in removed:
                    continue
                if s[left] == p[right]:
                    right += 1
                if right == n:
                    break
            return right == n
           

        left, right = 0, len(removable)
        res = 0
        while left <= right:
            middle = (left + right) // 2
         
            if isSubsequence(middle):
                left = middle + 1
                res = middle
            else:
                right = middle - 1
        return res