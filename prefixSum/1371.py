class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        v = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        curr = 0
        left = dict()
        left[0] = -1
        ans = 0
        for index, i in enumerate(s):
            if(i in v):
                curr ^= (1<<v[i])
            if(curr not in left):
                left[curr] = index
            else:
                ans = max(ans, index - left[curr])
        return ans