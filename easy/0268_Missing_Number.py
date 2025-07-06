class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expected = len(nums)*(len(nums)+1) // 2
        total = sum(nums)
        return expected - total
