class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        low = 0
        high = len(nums) -1

        while low <= high:

            mid = (high + low) // 2
            
            prev = nums[mid - 1] if mid > 0 else float('-inf')
            next_ = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
            
            if nums[mid] > prev and nums[mid] > next_:
                return mid
            elif nums[mid] < next_:
                low = mid + 1
            elif nums[mid] < prev:
                high = mid - 1
        
        return 0
