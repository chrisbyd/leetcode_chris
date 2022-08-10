class Solution:
    def carPooling(self, tripss: List[List[int]], capacity: int) -> bool:
        maxPass = 0 
        trips = [0] * 1001
        ans = []
        for np, f, t in tripss:
            trips[f] += np
            if t <= 1000:
                trips[t] -= np
        for i in range(1, 1001):
            trips[i] += trips[i-1]
        maxPass = max(trips)
        return True if maxPass <= capacity else False
            
        