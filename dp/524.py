from typing import List

class Solution:

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        a = sorted(dictionary, reverse= True)
        dictionary = sorted(a, key= len)
        def canForm(s, word):
            if not word:
                return True
            elif not s:
                return False
            elif word[0] not in s:
                return False
            else:
                index = s.index(word[0])
                return canForm(s[index+1:], word[1:])
        for word in reversed(dictionary):
            if canForm(s, word):
                return word
        return ""

sol = Solution()
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
s = "abpcplea"
dictionary = ["a","b","c"]
res = sol.findLongestWord(s, dictionary)
print(res)


        