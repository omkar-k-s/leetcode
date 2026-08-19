import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # max heap (store negative values)
        self.large = []  # min heap

    def addNum(self, num):
        # Add to max heap first
        heapq.heappush(self.small, -num)

        # Make sure every value in small <= every value in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0