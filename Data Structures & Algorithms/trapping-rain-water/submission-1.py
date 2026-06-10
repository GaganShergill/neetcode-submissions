class Solution:
    def trap(self, height: List[int]) -> int:
        bottom = []
        res = 0

        for right in range(len(height)):
            while bottom and height[right] > height[bottom[-1]]:
                b = bottom.pop()
                if not bottom:
                    break
                
                left = bottom[-1]
                min_height = min(height[left], height[right]) - height[b]
                res += min_height * (right - left - 1)
            
            bottom.append(right)
        
        return res

                
