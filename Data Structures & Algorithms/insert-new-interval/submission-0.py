class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x, y = newInterval
        flag = True
        for interval in intervals:
            i, j = interval
            if i <= x <= j or i <= y <= j or (x < i and y > j):
                x = min(x, i)
                y = max(y, j)
            else:
                if flag and (x < i and y < j):
                    res.append([x, y])
                    flag = False
                res.append(interval)
            
            print(x, y, res)
            
        if flag:
            res.append([x, y])
        

        return res