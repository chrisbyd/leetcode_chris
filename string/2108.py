from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ''
        for word in words:
            if word  == word[::-1]:
                return word
        return ans

sol = Solution()
words = ["abc","car","ada","racecar","cool"]
res= sol.firstPalindrome(words)
print(res)