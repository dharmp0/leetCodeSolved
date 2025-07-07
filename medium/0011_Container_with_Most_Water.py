class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) -1
        
        max_area = min(height[left], height[right]) * right - left

        while left < right:
    
            area = min(height[left], height[right]) * (right - left)
    
            if area > max_area:
                max_area = area
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_area
