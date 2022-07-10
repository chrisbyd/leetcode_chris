from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        for word in strs:
            min_length = min(min_length, len(word))
        ans = ''
        for i in range(min_length):
            equal = ''
            for word in strs:
                if equal == '':
                    equal = word[i]
                elif word[i] != equal:
                    return ans
            ans += word[i]
        return ans

sol = Solution() 
strs =  ["dog","racecar","car"]
res= sol.longestCommonPrefix(strs)
print(res)


        