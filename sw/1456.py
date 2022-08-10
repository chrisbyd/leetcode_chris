class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        start , ans ,  count = 0, 0, 0
        for i in range(k-1):
            if s[i] in vowels:
                count += 1
        for i in range(k-1, len(s)):
            if s[i] in vowels:
                count += 1
            ans = max(ans, count)
            if s[start] in vowels:
                count -= 1
            start += 1
        return ans
            
            