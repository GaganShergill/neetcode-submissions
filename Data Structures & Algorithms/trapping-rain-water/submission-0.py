class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # Stores indices
        res = 0
        
        for i in range(len(height)):
            # While current height is a "right wall" taller than the "bottom"
            while stack and height[i] > height[stack[-1]]:
                # 1. Identify the bottom of the pool
                bottom_idx = stack.pop()
                
                # 2. If no left wall exists, we can't trap water
                if not stack:
                    break
                
                # 3. Identify the left wall
                left_wall_idx = stack[-1]
                
                # 4. Calculate width and bounded height
                # Width is the distance between walls
                width = i - left_wall_idx - 1
                
                # Height is the min of the two walls minus the bottom height
                bounded_height = min(height[i], height[left_wall_idx]) - height[bottom_idx]
                
                res += width * bounded_height
            
            # Push current index to maintain decreasing order
            stack.append(i)
            
        return res
            



