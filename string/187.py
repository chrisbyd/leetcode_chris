from typing import List


# brutal force solution which will not be accepted 
# this one is o(n^2)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        for i in range(0, len(s) -9):
            window = s[i : i + 10]
            if window not in ans:
                for j in range(i+1, len(s) -9):
                    this_window = s[j: j+10]
                    if window == this_window:
                        ans.add(window)
                        break
        
        return list(ans)


sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = sol.findRepeatedDnaSequences(s)
print(res)

#actually we can solve it in on(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        tmp = set()
        ans = set()
        for i in range(0, len(s) -9):
            window = s[i : i + 10]
            if window in tmp:
                ans.add(window)
            else:
                tmp.add(window)
        return list(ans)

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = sol.findRepeatedDnaSequences(s)
print(res)


        