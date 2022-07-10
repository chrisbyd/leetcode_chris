import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hasht = {}
        stack = [s[0]]
        for i in range(len(s)):
            hasht[s[i]]=i

        for i in range(1, len(s)):
            while stack and s[i] not in stack and s[i] < stack[-1] and i < hasht[stack[-1]]:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])

        
        return "".join(stack)
        




sol = Solution()
s = "cbacdcbc"
res = sol.removeDuplicateLetters(s)
print(res)