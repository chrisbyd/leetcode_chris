from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(time):
            hour, minute = time.split(":")
            ans = int(hour) * 60 + int(minute)
            return ans
        converted_time = []
        for time in timePoints:
            c_time = convertToMinutes(time)
            converted_time.append(c_time)
            converted_time.append(1440 + c_time)
        converted_time.sort()
        ans = converted_time[1] - converted_time[0]
        for i in range(1, len(converted_time)):
            ans = min(ans, converted_time[i] - converted_time[i-1])
        return ans
        