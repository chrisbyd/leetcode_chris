from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o_map = {char : idx+1  for idx, char in enumerate(order)}
        o_map['0'] = 0
        n = len(words)
        
        def compareTwo(word1, word2):
            n_word1 = len(word1)
            n_word2 = len(word2)
            if n_word1 < n_word2:
                word1 += (n_word2  - n_word1) * '0'
            else:
                word2 +=  (n_word1 - n_word2) * '0'
            
            for i in range(n_word1):
                if o_map[word1[i]] > o_map[word2[i]]:
             
                    return False
                elif o_map[word1[i]] < o_map[word2[i]]:
                    break
            return True
                
        for i in range(n-1):
            if not compareTwo(words[i], words[i+1]):
                return False
        return True

sol = Solution()
words = ["hello","leetcode"]
order ="hlabcdefgijkmnopqrstuvwxyz"
res = sol.isAlienSorted(words ,order)
print(res)