import bisect
class RecentCounter:

    def __init__(self):
        self.counter = []
        self.count = 0
        

    def ping(self, t: int) -> int:
        self.counter.append(t)
        index = bisect.bisect_left(self.counter, t - 3000)
        self.count += 1
        return self.count -index
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)