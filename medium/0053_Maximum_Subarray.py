class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        at_max = float(-inf)

        for i in nums:
            curr_max = max(i, curr_max + i)
            at_max = max(at_max, curr_max)
        
        return at_max
