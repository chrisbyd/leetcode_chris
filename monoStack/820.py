from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        nwords = sorted(words, key = len, reverse = True)
        ans = []
        for word in nwords:
            length = len(word)
            find = False
            for string in ans:
                if len(string) < length:
                    break
                if string[-length:] == word:
                    find = True
                    break
            if find:
                continue
            else:
                ans.append(word)
        ans = '#'.join(ans)
        return len(ans) +1

class Solution(object):
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)