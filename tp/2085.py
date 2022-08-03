from typing import List


from collections import defaultdict
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        word1dict = defaultdict(int)
        word2dict = defaultdict(int)
        for word in words1:
            word1dict[word] += 1
        for word in words2:
            word2dict[word] += 1
        ans = 0
        for word in word1dict.keys():
            if word1dict[word] != 1:
                continue
            elif word2dict[word] != 1:
                continue
            else:
                ans += 1
        return ans
                
        