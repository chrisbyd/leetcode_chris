class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        s1dict, s2dict = defaultdict(int), defaultdict(int)
        for word in s1:
            s1dict[word] += 1
        for word in s2:
            s2dict[word] += 1
        ans = []
        for word in s1dict.keys():
            if s1dict[word] == 1 and word not in s2dict:
                ans.append(word)
        for word in s2dict.keys():
            if s2dict[word] == 1 and word not in s1dict:
                ans.append(word)
        return ans
        