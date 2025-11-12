class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority(lo: int, hi: int) -> int:
            if lo == hi:
                return nums[lo]
            
            mid = (lo + hi) // 2
            left = majority(lo, mid)
            right = majority(mid +1, hi)

            if left == right:
                return left
            
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right
            
        return majority(0, len(nums)-1)
