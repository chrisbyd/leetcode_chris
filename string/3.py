from typing import List
# the  codes are not concise
# needed to be refined tomorrow


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i,j = 0, 0
        count = 0
        current_window = set()
        max_length = 0
        while j < n:
            if i == j:
                current_window.add(s[j])
                count = 1
                max_length = count if count > max_length else max_length
                j += 1
            elif s[j] not in current_window:
                current_window.add(s[j])
                count += 1
                j+= 1
                max_length = count if count > max_length else max_length
            else:
                current_window.remove(s[i])
                i += 1
                count -= 1
        return max_length

sol = Solution()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r  = 0, 0
        max_count = 0
        charSet = set()
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
            elif l == r:
                charSet.add(s[r])
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
            if len(charSet) > max_count:
                max_count = len(charSet)
        return max_count


sol = Solution1()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)


        
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        max_count = 0
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while l != r:
                    if s[r] in charSet:
                        charSet.remove(s[l])
                        l += 1
                    else:
                        break
                charSet.add(s[r])
            if len(charSet) > max_count:
                max_count = len(charSet)
        return max_count


sol = Solution2()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        max_count = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_count = max(max_count, r- l +1)
        return max_count
        
            

sol = Solution3()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)







        