from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans, n, count, left  = float('inf'), 0, 0, 0
        cardSet = set()
        for right, num in enumerate(cards):
            if num not in cardSet:
                cardSet.add(num)
                count += 1
            else:
                while left < right and num in cardSet:
                    ans = min(ans, count + 1)
                    count -= 1
                    cardSet.remove(cards[left])
                    left += 1
                count += 1
                cardSet.add(num)
        return ans if ans != float('inf') else -1
                
        