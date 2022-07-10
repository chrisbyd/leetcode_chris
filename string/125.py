from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for character in s:
            char = character.lower()
            if char.isnumeric() or char.isalpha():
                ans.append(char)
        ans = ''.join(ans)
        r_ans = ans[::-1]
        if ans == r_ans:
            return True
        return False

sol = Solution()
s = "abc   ::~ cba"
res = sol.isPalindrome(s)
print(res)
