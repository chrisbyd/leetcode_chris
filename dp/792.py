from typing import List


# memory limit exceed
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def matchSub(s, word):
            if len(word) == 1:
                if word in s:
                    return True
                return False
            else:
                if word[0] in  s:
                    index = s.index(word[0])
                    return True if matchSub(s[index+1:], word[1:]) else False
                else:
                    return False
        ans = 0
        for word in words:
            if matchSub(s, word):
                ans += 1
        return ans

sol = Solution()
s = "abcde"
words = ["a","bb","acd","ace"]
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
res = sol.numMatchingSubseq(s, words)
print(res)

# accepted but it is too slow
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def matchSub(s, word):
            for i in range(len(word)):
                if word[i] not in s:
                    return False
                index = s.index(word[i])
                s = s[index+1:]
            return True
            
        ans = 0
        for word in words:
            if matchSub(s, word):
                ans += 1
        return ans

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
res = sol.numMatchingSubseq(s, words)
print(res)

# using  a trie