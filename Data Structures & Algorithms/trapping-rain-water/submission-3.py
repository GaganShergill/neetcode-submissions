class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i in range(len(height)):
            max_left = height[i]
            for j in range(i):
                max_left = max(max_left, height[j])
        
            
            max_right = height[i]
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            
            water += min(max_left, max_right) - height[i]
        
        return water