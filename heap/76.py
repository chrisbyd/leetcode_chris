from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        l, r = 0, 0 
        if not t or not s: return False
        ans, length = "", float('inf')
        dict_t = Counter(t)
        window_counts = defaultdict(int)
        formed = 0
        required = len(dict_t)
        while r < len(s):
            character = s[r]
            if character in dict_t: 
                window_counts[character] += 1
                if window_counts[character] == dict_t[character]:
                    formed += 1
        
            while l <= r and formed == required:
                character = s[l]
                if r- l + 1 < length:
                    length = r -l + 1
                    ans = s[l: r+ 1]
                if character in dict_t:
                    window_counts[character] -= 1
                    if window_counts[character] < dict_t[character]:
                        formed -= 1
                l += 1
            r += 1
        return ans

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = sol.minWindow(s,t)
print(res)