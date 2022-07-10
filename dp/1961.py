from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for word in words:
            length = len(word)
            if s[:length] != word:
                break
            else:
                s = s[length:]
        return True if not s else False
        