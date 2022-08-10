from collections import Counter, defaultdict
class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        find = {}
        ans = float('inf')
        for char in count:
            if count[char] > len(s) / 4:
                find[char]  = count[char] - len(s) / 4
        if not find: return 0
        print(find)
        start = 0
        find_count = defaultdict(int)
        xcount = 0
        for i, val in enumerate(s):
            if val in find:
                if  find_count[val] == find[val] - 1:
                    xcount += 1
                find_count[val] += 1
            print(find_count, xcount)
            if xcount == len(find):
                print("find already")
                while start < i:
                    if s[start] in find:
                        if find_count[s[start]] == find[s[start]]:
                            break
                        else:
                            find_count[s[start]] -= 1
                    start += 1
                    ans = min(ans, i - start + 1)
                ans = min(ans, i - start + 1)
        return ans
            
            
sol = Solution()
s = "WWWEQRQEWWQQQWQQQWEWEEWRRRRRWWQE"
print(len(s))
res = sol.balancedString(s)
print(res)