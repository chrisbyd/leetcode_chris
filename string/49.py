from typing import List

# The first algorithm with sort O(n2)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        new_strs = [''.join(sorted(word)) for word in strs]
        visited = set()
        for i in range(len(strs)):
            if i not in visited:
                visited.add(i)
                res = [strs[i]]
            else:
                continue
            for j in range(i+1, len(strs)):
                if new_strs[i] == new_strs[j]:
                    res.append(strs[j])
                    visited.add(j)
            ans.append(res)
        return ans

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["a"]
res = sol.groupAnagrams(strs)
print(res)


# using sorting and hashing map

import collections
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hmap[sorted_word].append(word)
        ans = hmap.values()

        return list(ans)


sol = Solution1()
strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["a"]
res = sol.groupAnagrams(strs)
print(res)
        
