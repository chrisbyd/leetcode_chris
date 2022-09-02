from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qr = deque([i for i in range(n) if senate[i] == 'R'])
        qd = deque([i for i in range(n) if senate[i] == 'D'])
        while qr and qd:
            r = qr.popleft()
            d = qd.popleft()
            if r < d:
                qr.append(r + n)
            else:
                qd.append(d + n)
        return "Radiant" if not qd else "Dire"
            