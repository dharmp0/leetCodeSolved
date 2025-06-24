class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        right = len(nums) - 1

        i  = 0
        while i <= right:
            if nums[i] == 0:
                del nums[i]
                right -= 1
                nums.append(0)
            else:
                i+=1
