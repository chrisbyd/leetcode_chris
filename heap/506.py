class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals =  ["Gold Medal","Silver Medal","Bronze Medal"]
        rank = sorted(score)[::-1]
        rankdict = {score:i for i, score in enumerate(rank)}
        ans = []
        for s in score:
            r = rankdict[s]
            if r < 3:
                ans.append(medals[r])
            else:
                ans.append(str(r+1))
        return ans
        