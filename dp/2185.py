from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        ans = 0
        for word in words:
            ans += 1 if word[:length] == pref else 0
        return ans