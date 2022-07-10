from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        try:
            ans =  haystack.index(needle)
        except ValueError:
            return -1
        return ans
        


sol = Solution()
haystack = "hello"
needle = "ab"
res = sol.strStr(haystack, needle)
print(res)

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i:i+ length] == needle:
                        return i
            return -1
    

sol = Solution1()
haystack = "helll"
needle = "lo"
res = sol.strStr(haystack, needle)
print(res)