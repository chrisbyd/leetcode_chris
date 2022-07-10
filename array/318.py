from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]
        mp = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                inter_set = word_sets[i] & word_sets[j]
                if len(inter_set) == 0:
                    res = len(words[i]) * len(words[j])
                    if res > mp:
                        mp = res
        return mp

sol = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
res = sol.maxProduct(words)
print(res)
        