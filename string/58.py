from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        encounted = False
        count = 0
        for character in reversed(s):
            if encounted and character == " ":
                return count
            elif character != " ":
                encounted = True
                count += 1
        return count 

sol = Solution()

s = "Hello World  "
res = sol.lengthOfLastWord(s)
print(res)