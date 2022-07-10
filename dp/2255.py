from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words:
            length = len(word)
            if word == s[:length]: 
                ans += 1
        return ans