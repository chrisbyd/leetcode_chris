import collections
import enum

# a naive solution
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ans = ""
        bulls_set = set()
        for idx, (a1, a2) in enumerate(zip(secret, guess)):
            if a1 == a2:
                bulls_set.add(idx)
        hmap = collections.defaultdict(list)
        for idx, a2 in enumerate(guess):
            hmap[a2].append(idx)
        for item in bulls_set:
            hmap[secret[item]].remove(item)
        ans += str(len(bulls_set)) + 'A'
        
        count = 0
        for idx, a1 in enumerate(secret):
            if idx not in bulls_set:
                if a1 in hmap and  len(hmap[a1]) != 0:
                    count += 1
                    hmap[a1].pop()
        ans += str(count) + 'B'

        return ans

sol = Solution()
secret = "1111"
guess = "0111"
res = sol.getHint(secret, guess)
print(res)

# a standard solution

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = 0
        secret = list(secret)
        guess = list(guess)
        ans = ''
        bullset = []
        for idx, (a1, a2) in enumerate(zip(secret, guess)):
            if a1 == a2:
                bullset.append(a1)
                count += 1
        
        for  a in bullset:
            secret.remove(a)
            guess.remove(a)
        ans += str(count) + 'A'
        count = 0
        for num in secret:
            if num in guess:
                count += 1
                guess.remove(num)
        ans += str(count) + 'B'
        return ans


sol = Solution()
secret = "1111"
guess = "0111"
res = sol.getHint(secret, guess)
print(res)