class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        left, right = 0, len(self.intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            e = self.intervals[mid]
            if e[0] <= value <= e[1]: return
            elif value < e[0]:right = mid - 1
            else:left = mid + 1
        pos = left
        self.intervals.insert(pos, [value, value])
        if pos + 1 < len(self.intervals) and value + 1 == self.intervals[pos+1][0]:
            self.intervals[pos][1] = self.intervals[pos+1][1]
            del self.intervals[pos+1]
        if pos - 1 >= 0 and value - 1 == self.intervals[pos-1][1]:
            self.intervals[pos-1][1] = self.intervals[pos][1]
            del self.intervals[pos]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()