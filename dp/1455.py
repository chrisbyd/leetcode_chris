from typing import List

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        length = len(searchWord)
        for i, word in enumerate(sentence.split()):
            if searchWord == word[:length]:
                return i + 1
        return -1
            
        