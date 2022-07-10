class Solution:
    def checkIsSubsequence(self, s1, s2):
        m, n = len(s1), len(s2)
        i, j = 0, 0
        while i < m and j < n:
            if s1[i] == s2[j]:
                i += 1
            j += 1
        if i == m:
            return True
        return False
                    
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(reverse =True, key = len)
        n = len(strs)
        for i in range(n):
            ans = 0
            for j in range(n):
                if i == j: continue
                if self.checkIsSubsequence(strs[i], strs[j]):
                    ans = 1
            if not ans:
                return len(strs[i])
        return -1
                
        