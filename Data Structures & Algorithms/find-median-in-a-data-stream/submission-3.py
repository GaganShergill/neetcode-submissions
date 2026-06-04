class MedianFinder:

    def __init__(self):
        self.minR = []
        self.maxL = []

    def addNum(self, num: int) -> None:
        if self.minR and num > self.minR[0]:
            heapq.heappush(self.minR, num)
        else:
            heapq.heappush(self.maxL, -num)

        if len(self.maxL) > len(self.minR) + 1:
            x = -heapq.heappop(self.maxL)
            heapq.heappush(self.minR, x)
        elif len(self.minR) > len(self.maxL) + 1:
            x = heapq.heappop(self.minR)
            heapq.heappush(self.maxL, -x)
        

    def findMedian(self) -> float:
        if len(self.maxL) > len(self.minR):
            return -self.maxL[0]
        elif len(self.minR) > len(self.maxL):
            return self.minR[0]
        else:
            x = self.minR[0]
            y = -self.maxL[0]
            return (x+y)/2
        
        
        