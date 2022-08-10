class Solution:
    def maxRepOpt1(self, text: str) -> int:
        first_occurence,last_occurence = {},{}
        ans,prev,count = 1,0,0
        n = len(text)
        
        for i in range(n):
            if text[i] not in first_occurence: first_occurence[text[i]] = i
            last_occurence[text[i]] = i
            
        for i in range(n+1):
            if i < n and text[i] == text[prev]:
                count += 1
            else:
                if first_occurence[text[prev]] < prev or last_occurence[text[prev]] > i : count += 1
                ans = max(ans,count)
                count = 1
                prev = i
        
        def someWork(item,before,after):
            count = 0
            while before >= 0 and text[before] == item: 
                count += 1
                before -= 1
            while after < n and text[after] == item:
                count += 1
                after += 1
            if first_occurence[item] <= before or last_occurence[item] >= after:count+=1
            return count
        
        for i in range(1,n-1):
            ans = max(ans,someWork(text[i+1],i-1,i+1))
        return ans


##### with intervals
from collections import defaultdict
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        intervals = defaultdict(list)
        prev, start = ' ', 0
        for i, char in enumerate(text):
            if char != prev and i != 0:
                intervals[prev].append((start, i))
                start = i
            prev = char
        intervals[prev].append((start, i+1))
        ans = 0
        print(intervals)
        ### for each letter
        for ch in intervals:
            indices = intervals[ch]
            n = len(indices)
            third_interval_letter = n > 2
            previ, prevj = indices[0]
            ans = max(ans, prevj - previ )
            
            for i in range(1, n):
                curi, curj = indices[i]
                if curi - prevj == 1:
                    ans = max(ans, curj - previ  + third_interval_letter - 1)
                else:
                    ans = max(ans, curj - curi+1, prevj - previ + 1)
                previ, prevj = curi, curj

        return ans
                
                
sol = Solution()
text = "ababa"
res = sol.maxRepOpt1(text)
print(res)
### with grouping
