class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ, stack, visited = {}, [], set()
        for i, char in enumerate(s):
            last_occ[char] = i
        for i, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                    ochar = stack.pop()
                    visited.remove(ochar)
                print(stack)

                stack.append(char)
                visited.add(char)
        return ''.join(stack)
        
sol = Solution()
s = "bcabc"
res = sol.removeDuplicateLetters(s)
print(res)