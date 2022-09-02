class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, ans, count = 0, 0, 0
        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                count += 1
                ans = max(ans, count)
            else:
                while left < right:
                    charSet.remove(s[left])
                    count -= 1
                    left += 1
                    if s[right] not in charSet:
                        charSet.add(s[right])
                        count += 1
                        break

        return ans

sol = Solution()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)