from heapq import heappush, heappop

class SeatManager:
    def __init__(self, n: int):
        self.seats = [i + 1 for i in range(n)]

    def reserve(self) -> int:
        seat = heappop(self.seats)
        return seat
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)