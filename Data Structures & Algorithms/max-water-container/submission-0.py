class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxArea = 0
        while i < j:
            minSide = min(heights[i], heights[j])
            maxArea = max(maxArea, minSide*(j-i))
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
            
        
        return maxArea
